# OCR 识别文字
import cv2
import pytesseract

def ocr_img():
    """ 识别图片文字 """
    image = cv2.imread(r"D:\A_Image_Saved\Cap_YangFan46.png")
    cv2.imshow("image", image)

    text = pytesseract.image_to_string(image, lang="chi_sim")
    print(text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ocr_video():
    """ 识别视频文字（速度较慢，需优化） """
    video_path = r"D:\A_Files_Saved\ScreenRecord\test001.mp4"
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No more frames")
            break
        cv2.imshow("Video", frame)
        text = pytesseract.image_to_string(frame, lang='chi_sim')
        print(text)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
