# 获取视频信息

import cv2

video = cv2.VideoCapture(r"D:\A_Image_Saved\emotion\emotion2.mp4")
# 显示帧数
print('帧数：', video.get(cv2.CAP_PROP_FRAME_COUNT))
# 显示帧率
print('帧率：', video.get(cv2.CAP_PROP_FPS))
# 显示尺寸
print('尺寸：', video.get(cv2.CAP_PROP_FRAME_WIDTH), video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 显示时长
print('时长：', video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS))
# 显示视频
while True:
    ret, frame = video.read()
    if ret:
        cv2.imshow("Video", frame)
    if cv2.waitKey(int(1000/video.get(cv2.CAP_PROP_FPS))) == ord('q'):
        break
