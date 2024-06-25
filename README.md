# 环境配置
python3.8 版本  
安装依赖 `pip install -r requirements.txt`

# 仓库文件介绍
## A FOLDER FOR TRAINING
将图片分别放入image的两个文件夹，标签分别放入labels的两个文件夹，修改data.yaml中train和val的路径，改为images下两个文件夹的绝对路径。  
runs 文件夹存放了三次训练的结果。
### 数据集获取：
链接：https://pan.baidu.com/s/1DVOMR3C0WRl3cAvsoeLwBg?pwd=mjks   
提取码：mjks  
两个分类：0 enemy(头)，1 body(人)
## model
三次训练结果的`best.pt`  
v5 v8分别为相同小数据集yolov5 yolov8训练100轮结果。  
v8_300 为最终数据集训练300轮结果。
## robot  
mouse.py: 鼠标控制程序。打开cs2游戏后运行（开始运行时cs2窗口不能小窗化），按ctrl+c终止。  
81行可修改选用模型，cpu推理删除83行，86 87行修改置信域, 88行修改索敌范围（距离准星）。  
## video
video_save.py: 输入视频测试。7 8行修改文件路径，16行修改选用模型。  

# 训练验证指令
## 训练（下方指令结果为最终模型）
yolo task=detect mode=train imgsz=640 model=yolov8.yaml data=data.yaml epochs=300 batch=8 name=v8_300  

## 验证（xxx为'.pt模型路径'）
yolo detect val model=`xxx` data=data.yaml

## 模型导出（没有用到）
yolo export model=`xxx` format=onnx

