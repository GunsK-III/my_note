# 2024/07/02
# 捕获屏幕，调用训练好的yolov3模型捕获屏幕，对画面中的人物进行识别与预测，并操作鼠标完成移动和点击（CS AI外挂）
import cv2
import numpy as np
import pyautogui

scr_width, scr_height = pyautogui.size()

# 加载模型
net = cv2.dnn.readNet(r"D:\NewFolder\Py_Folder\yolo_obj_detection\yolo\yolov3.weights",
                      r"D:\NewFolder\Py_Folder\yolo_obj_detection\yolo\yolov3.cfg")

with open(r"D:\NewFolder\Py_Folder\yolo_obj_detection\yolo\coco.names", 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# 获取输出层信息
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

while True:
    img = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    frame = cv2.resize(frame, (scr_width, scr_height))

    # 图像预处理
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # 解析输出并绘制边框
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.7:
                # 获取边界框的坐标
                center_x = int(detection[0] * scr_width)
                center_y = int(detection[1] * scr_height)
                w = int(detection[2] * scr_width)
                h = int(detection[3] * scr_height)
                # 边界框的左上角坐标
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

                # 检查是否识别到指定目标
                if classes[class_id] == 'person':
                    # 将中心坐标转换为屏幕坐标
                    screen_center_x, screen_center_y = center_x, center_y
                    print(center_x, ",", center_y)        # 输出坐标
                    pyautogui.moveTo(screen_center_x, screen_center_y)        # 移动鼠标
                    # pyautogui.leftClick()         # 点击鼠标

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)    # 置信度阈值0.5，IoU阈值0.4

    font = cv2.FONT_HERSHEY_PLAIN       # 字体
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))        # 随机颜色

    # 画框
    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label + " " + confidence, (x, y + 20), font, 2, color, 2)

    cv2.imshow('Screen Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
