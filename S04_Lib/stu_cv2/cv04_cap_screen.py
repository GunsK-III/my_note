"""录制屏幕"""

import cv2
import numpy as np
import pyautogui

screen_width = 1080
screen_height = 675

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用mp4格式
fps = 15.0
out = cv2.VideoWriter('screen_capture.mp4', fourcc, fps, (screen_width, screen_height))

while True:
    # 使用pyautogui捕获屏幕
    img = pyautogui.screenshot()
    # 转换为OpenCV格式（BGR）
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    frame = cv2.resize(frame, (screen_width, screen_height))

    out.write(frame)
    cv2.imshow('Screen Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
