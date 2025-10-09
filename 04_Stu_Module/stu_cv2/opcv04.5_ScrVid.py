import cv2
import pyautogui
import numpy as np
import time

screen_size = (pyautogui.size().width, pyautogui.size().height)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(r'D:\A_Files_Saved\videos\output.mp4', fourcc, 5.0, (800, 600))

cv2.namedWindow('hidden', cv2.WINDOW_NORMAL)
cv2.resizeWindow('hidden', 1, 1)
cv2.moveWindow('hidden', -1000, -1000)

try:
    while True:
        start_time = time.time()  # 记录开始时间
        img = pyautogui.screenshot(region=(0, 0, 800, 600))
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

        # 计算本次循环耗时，并确保下次循环前等待的时间满足5 fps要求
        elapsed_time = time.time() - start_time
        sleep_time = max(0, (1 / 5) - elapsed_time)
        time.sleep(sleep_time)

        if cv2.waitKey(1) == ord('q'):
            break

finally:
    out.release()
    cv2.destroyAllWindows()
