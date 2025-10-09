# numpy在图像处理中的一些基本应用
import cv2
import numpy as np
from PIL import Image

# img = cv2.imread(r"D:\A_Image_Saved\eagle.jpg")
# print(img)      # 对opencv导入的图片，这回输出一个三维数组表示像素数据，三个维度分别表示图像宽度、高度、颜色通道数。
# print(img[50, 50])     # opencv中默认使用的是BGR，如果用的是PIL，则是RGB
# print('----------------')
img2 = Image.open(r"D:\A_Image_Saved\eagle.jpg")
# print(img2)         # 这里会输出图像的信息字符串。
img2 = np.array(img2)       # 对PIL导入的图片，需要先转换为numpy数组才能进行操作。
# print(img2)        # 返回一个三维数组，表示像素数据。
# img_r = img2[:, :, 0]       #
# Image.fromarray(img_r).show()       # 创建并显示一个临时图片文件

