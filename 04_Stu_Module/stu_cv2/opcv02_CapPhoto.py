# 调用摄像头，多次拍照片、命名
import cv2
import time

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

photo_count = 1  # 用于计数已保存的照片数量

while True:
    ret, frame = cap.read()
    # 转灰度
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        print("无法读取图像")
        break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # 生成唯一的文件名，包含时间戳
        file_name = f"CapPhoto_{time.strftime('%Y%m%d%H%M%S')}.jpg"
        # 使用格式控制符%，可以把图片保存到指定文件夹，然而用字符串相加的方式写保存路径，则会保存到最后一个文件夹外面...
        out_path = r"D:\NewFolder\Py_Folder\files2\%s" % file_name
        # 比如说下面这个方式就不行。
        # out_path = r"D:\NewFolder\pythonProject1\.venv\Files_Crate\AddFolder" + file_name
        cv2.imwrite(out_path, frame)
        print(f"照片 {file_name} 已保存到本地")
        photo_count += 1
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
