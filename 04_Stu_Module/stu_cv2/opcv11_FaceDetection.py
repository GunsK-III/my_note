# @Title:   Face Detection
# @Author:  FanDC(Yang Fan 46)
# @Email:   a2078769713@outlook.com
# @Time:    2024/06/07
# --------------------------------------

import cv2

face_cascade = cv2.CascadeClassifier(r"D:\NewFolder\pythonProject1\.venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"D:\NewFolder\pythonProject1\.venv\Lib\site-packages\cv2\data\haarcascade_eye.xml")

# cap = cv2.VideoCapture(r"D:\A_Files_Saved\videos\vid04.mp4")
cap = cv2.VideoCapture(0)
# 求取视频帧率
# fps = cap.get(cv2.CAP_PROP_FPS)
while True:
    ret, frame = cap.read()
    if ret:
        # frame = cv2.resize(frame, (495, 880))     # 改变视频尺寸
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        print('当前帧检测到人脸数量:', len(faces))
        cv2.imshow('DETECTION', frame)
    else:
        break
    if cv2.waitKey(int(10)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
