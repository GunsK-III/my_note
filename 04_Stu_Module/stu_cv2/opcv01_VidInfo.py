# 1 显示视频信息
# 2 调用摄像头,多次拍照、命名
# 3 每隔20帧保存一张视频帧
# 4 打开摄像头,录制视频
# 5 图片汉字识别

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
