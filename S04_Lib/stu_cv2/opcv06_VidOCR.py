# 视频汉字识别
import cv2
import pytesseract

video_path = r"D:\A_Files_Saved\ScreenRecord\vid_yf46.mp4"
cap = cv2.VideoCapture(video_path)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video", frame)
    text = pytesseract.image_to_string(frame, lang='chi_sim')
    print(text)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
