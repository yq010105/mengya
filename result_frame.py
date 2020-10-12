from func import result as re
import cv2
import time

def rf():
    while True:
        video = cv2.VideoCapture(0)
        re.video_show(video,100)    # 100 是窗口停留的时间大概 3.638s左右
        # 图像识别，模板匹配 生成一个frame.jpg文件
        # 根据生成的frame.jpg 进行指针的识别
        time.sleep(5)

if __name__ == "__main__":
    rf()