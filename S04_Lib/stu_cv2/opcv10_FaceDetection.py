# 对图片进行面部识别
import cv2

face_cascade = cv2.CascadeClassifier(r"D:\NewFolder\pythonProject\study_note\.venv\Lib\site-packages\cv2\data"
                                     r"\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"D:\NewFolder\pythonProject\study_note\.venv\Lib\site-packages\cv2\data"
                                    r"\haarcascade_eye.xml")

img = cv2.imread(r"D:\A_Image_Saved\emotion\Carrey.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

img = cv2.resize(img, (360, 500))
cv2.imshow('img', img)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.waitKey(0)
cv2.destroyAllWindows()
