import ctypes
import math
import numpy as np
from ultralytics import YOLO
import win32api
import win32con
import win32gui
import win32ui
import time
from ctypes import windll
from pynput.mouse import Controller

 
class Point():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
 
 
class Line(Point):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
 
    def getlen(self):
        changdu = math.sqrt(math.pow((self.x1 - self.x2), 2) + math.pow((self.y1 - self.y2), 2))
        return changdu


def capture_screen(window_name):
    windll.user32.SetProcessDPIAware()    
    hwnd = win32gui.FindWindow(None, window_name)
    # win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    # win32gui.SetForegroundWindow(hwnd)
    try:
        # Get window dimensions

        left, top, right, bottom = win32gui.GetClientRect(hwnd)
        w = right - left
        h = bottom - top

        hwnd_dc = win32gui.GetWindowDC(hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()
        bitmap = win32ui.CreateBitmap()
        bitmap.CreateCompatibleBitmap(mfc_dc, w, h)
        save_dc.SelectObject(bitmap)

        result = windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), 3)

        bmpinfo = bitmap.GetInfo()
        bmpstr = bitmap.GetBitmapBits(True)

        img = np.frombuffer(bmpstr, dtype=np.uint8).reshape((bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4))
        img = np.ascontiguousarray(img)[..., :-1]  

        if not result:  # result should be 1
            win32gui.DeleteObject(bitmap.GetHandle())
            save_dc.DeleteDC()
            mfc_dc.DeleteDC()
            win32gui.ReleaseDC(hwnd, hwnd_dc)
            raise RuntimeError(f"Unable to acquire screenshot! Result: {result}")

        return img, w, h
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

  
  

def main():
    try:
        ctypes.windll.shell32.IsUserAnAdmin()
    except:
        print("need access!")
        return

    model_path = '..\\model\\v8_300.pt'
    model = YOLO(model_path)
    model.to('cuda')
    window_name = "Counter-Strike 2"

    headscore = 0.7
    bodyscore = 0.6 #confidence
    dis = 300 #search range
    start = time.time()
    flag = 0
    ctrl_c_pressed = False
    
    while not ctrl_c_pressed:
        if win32api.GetAsyncKeyState(ord('C')) and win32api.GetAsyncKeyState(win32con.VK_CONTROL):
            ctrl_c_pressed = True
        # if time.time() - start >= 20:
        #     flag = 1
        #     break
        screen, game_width, game_height = capture_screen(window_name)
        # cv2.imshow(window_name, screen)
        # break
        results = model(screen)[0]
        

        headlist = []
        bodylist = []
        newlist = []
        
        for result in results.boxes.data.tolist():
            xmin, ymin, xmax, ymax, score, class_id = result

            if class_id == 0.0 and score >= headscore:
                headlist.append([int(xmin), int(ymin), int(xmax), int(ymax), score])
            elif class_id == 1.0 and score >= bodyscore:
                bodylist.append([int(xmin), int(ymin), int(xmax), int(ymax), score])



        if len(headlist) > 0:
            newlist = headlist
        elif len(bodylist) > 0:
            newlist = bodylist
            
        if len(newlist) > 0:
            cdList = []
            xyList = []
            for listItem in newlist:
                xindex = int(listItem[2] - (listItem[2] - listItem[0]) / 2)
                yindex = int(listItem[3] - (listItem[3] - listItem[1]) / 2)
                mouseModal = Controller()
                x, y = mouseModal.position
                L1 = Line(x, y, xindex, yindex)
                cdList.append(int(L1.getlen()))
                xyList.append([xindex, yindex, listItem[0], listItem[1], listItem[2], listItem[3]])
            minCD = min(cdList)
            if minCD < dis:
                for cdItem, xyItem in zip(cdList, xyList):
                    if cdItem == minCD:
                        # if win32api.GetAsyncKeyState(0x01):
                        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(xyItem[0] - game_width // 2),
                                                 int(xyItem[1] - (game_height) // 2), 0, 0)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                        time.sleep(0.00001)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                        break


        time.sleep(0.001)
        
    print(flag)

if __name__ == "__main__":
    main()
