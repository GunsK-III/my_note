# 打开摄像头，录制视频（保存视频帧）,保存到相对路径下
import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Unable to open camera")
    exit()

# 设置视频帧的宽度和高度
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 视频保存相关参数
save_path = 'captured_video.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 视频编码格式，这里使用 XVID
out = cv2.VideoWriter(save_path, fourcc, 30.0, (640, 480))  # 输出视频文件

while True:
    ret, frame = cap.read()  # 读取视频帧
    if not ret:
        print("Error: Unable to read frame")
        break
    cv2.imshow('Frame', frame)  # 显示视频帧
    out.write(frame)    # 将视频帧写入输出视频文件
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 'q' 键退出循环
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
