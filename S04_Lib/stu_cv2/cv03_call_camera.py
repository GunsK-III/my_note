# 调用摄像头，多次拍照片、命名
import cv2
import time


def cap_photo():
    """ 调用摄像头拍照 """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        exit()

    photo_count = 1

    while True:
        ret, frame = cap.read()
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       # 转灰度
        if not ret:
            print("无法读取图像")
            break
        cv2.imshow('frame', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            # 生成唯一的文件名，包含时间戳
            file_name = f"CapPhoto_{time.strftime('%Y%m%d%H%M%S')}.jpg"
            # 使用格式控制符%，可以把图片保存到指定文件夹，
            out_path = r"D:\NewFolder\Py_Folder\files2\%s" % file_name
            # 然而用字符串相加的方式写保存路径，则会保存到最后一个文件夹外面。不可用
            # out_path = r"D:\NewFolder\pythonProject1\.venv\Files_Crate\AddFolder" + file_name
            cv2.imwrite(out_path, frame)
            print(f"照片 {file_name} 已保存到本地")
            photo_count += 1
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def cap_video():
    """ 调用摄像头录像 """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to open camera")
        exit()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    save_path = 'my_video.mp4'  # 文件名后缀应和编码格式保持对应关系
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 视频编码格式，这里使用 mp4v
    out = cv2.VideoWriter(save_path, fourcc, 30.0, (640, 480))

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame")
            break
        cv2.imshow('Frame', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 'q' 键退出循环
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
