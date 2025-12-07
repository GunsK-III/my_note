""" name: 课设 - 目标检测（图片）
    date: 2024/06/02
    desc: 对图片内容进行目标检测
"""
import cv2
import numpy as np

# 加载模型
net = cv2.dnn.readNet(r"D:\NewFolder\Py_Folder\yolo_obj_detection\yolo\yolov3.weights",
                      r"D:\NewFolder\Py_Folder\yolo_obj_detection\yolo\yolov3.cfg")

# 加载类别标签
with open(r"D:\NewFolder\Py_Folder\yolo_obj_detection\yolo\coco.names", 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# 获取输出层信息
layer_names = net.getLayerNames()
output_layers_indices = net.getUnconnectedOutLayers()
if isinstance(output_layers_indices, np.ndarray):  # 注意！！！由于版本差异，有时i会返回数值，有时i返回的是数组/列表。
    output_layers = [layer_names[i - 1] for i in output_layers_indices]
else:
    output_layers = [layer_names[i[0] - 1] for i in output_layers_indices]

# 读取图片
image_path = input("输入图片路径：")
image = cv2.imread(image_path)
height, width, channels = image.shape

# 图像预处理
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# 解析输出并绘制边界框
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]  # 置信度
        if confidence > 0.5:
            # 边界框的坐标
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(classes), 3))

det_obj = []

if len(indexes) > 0:
    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str(round(confidences[i], 2))
        color = colors[i]
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(image, label + " " + confidence, (x, y + 30), font, 3, color, 3)
        # print("检测到的物体有：", label, end="\t")
        det_obj.append(label)

print("检测到的物体有：", '、'.join(det_obj))

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
