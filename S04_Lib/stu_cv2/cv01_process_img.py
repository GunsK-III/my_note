# Opencv 图像处理基础操作
import cv2

image = cv2.imread(r"D:\A_Image_Saved\tree.png")

cv2.namedWindow("Tree", cv2.WINDOW_NORMAL)    # 窗口可调
cv2.imshow("Tree", image)
a = cv2.waitKey(0)
cv2.destroyAllWindows()     # 销毁窗口，释放资源

# 转灰度
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 查看尺寸
# print(image.shape)     # >>(720,1280,3)

# 缩放
# resized = cv2.resize(image, (540, 360))      # 常用
# gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Resized", resized)
# cv2.waitKey(0)

# 裁剪
# cropped = image[0:300, 0:400]
# cv2.imshow("Cropped", cropped)
# cv2.waitKey(0)

# 绘制
# image2 = resized
# cv2.line(image2, (0, 0), (480, 360), (0,255,0), 1)
# cv2.rectangle(image2, (24, 18), (120, 90), (0, 0, 255), 2)
# cv2.circle(image2, (240,180), 50, (255, 0, 0), 2)
# cv2.putText(image2,'Hello', (240,30),0, 1,(255,255,255),2,1)
# cv2.imshow("image2", image2)
# cv2.waitKey(0)

# 图像特征提取
# corners = cv2.goodFeaturesToTrack(gray, 500, 0.1, 10)
# for i in corners:
#     x, y = i.ravel()
#     cv2.circle(image, (int(x), int(y)), 3, (0, 0, 255), -1)
# cv2.imshow("Corners", image)
# cv2.waitKey(0)

# 梯度算法
# image = cv2.resize(image, (360, 240))             缩放
# laplacian = cv2.Laplacian(gray, cv2.CV_64F)
# edge = cv2.Canny(gray, 100, 200)
# cv2.imshow("image", image)
# cv2.imshow("gray", gray)
# cv2.imshow("Laplacian", laplacian)
# cv2.imshow("Edge", edge)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 阈值算法
# ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)        # 基础阈值
# binary_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11, 2) # 通过自适应阈值处理，将图像转换为高质量的二值图像
# ret2,thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)       # 大津算法
# cv2.imshow("Image", image)
# cv2.imshow("Gray", gray)                      #灰度图
# cv2.imshow("Threshold", thresh)               #阈值图（70）
# cv2.imshow("Binary", binary_adaptive)         #自适应阈值，不同区域有不同阈值，所以无阈值变量
# cv2.imshow("Threshold_Otsu", thresh_otsu)     #大津算法，最佳阈值 == ret2
# cv2.imwrite(r"D:\A_Image_Saved\k02_thresh_otsu.jpg", thresh_otsu)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 形态学算法
# image3 = cv2.imread(r"C:\Users\BMF\Pictures\Screenshots\FanDC.png")
#
# #黑白反转。将像素值大于阈值的设为最大值，小于等于阈值的设为0，生成一个新的二值化图像。函数返回二值化图像和阈值值
# ret3,binary = cv2.threshold(image3, 250, 255, cv2.THRESH_BINARY_INV)
# kernel = np.ones((5,5),np.uint8)   # 操作核
# erosion = cv2.erode(binary,kernel)       # 使用kernel腐蚀binary图像
# dilation = cv2.dilate(binary,kernel)
#
# cv2.imshow("image", image3)      # 显示原图
# cv2.imshow("binary",binary)      # 二值化图像
# cv2.imshow("erosion",erosion)    # 腐蚀图像
# cv2.imshow("dilation",dilation)  # 膨胀图像
# cv2.waitKey(0)

