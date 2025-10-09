import cv2
import pytesseract

image = cv2.imread(r"D:\A_Image_Saved\Cap_YangFan46.png")
cv2.imshow("image", image)

# pytesseract.pytesseract.tesseract_cmd = r"D:\NewFolder\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(image, lang="chi_sim")
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()