"""录制屏幕"""

import cv2
import numpy as np
import pyautogui

# 捕获分辨率
screen_width = 1080
screen_height = 675

# 视频保存参数
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用mp4格式
fps = 15.0
out = cv2.VideoWriter('screen_capture.mp4', fourcc, fps, (screen_width, screen_height))  # 输出文件名、编解码器、帧率、压缩后的分辨率

while True:
    # 使用pyautogui捕获屏幕
    img = pyautogui.screenshot()
    # 转换为OpenCV格式（BGR）
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    frame = cv2.resize(frame, (screen_width, screen_height))

    # 写入视频文件
    out.write(frame)

    cv2.imshow('Screen Capture', frame)

#     # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
