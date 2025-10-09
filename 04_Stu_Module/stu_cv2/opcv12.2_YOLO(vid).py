# 对视频进行目标检测
import cv2
import numpy as np

net = cv2.dnn.readNet(r"D:\NewFolder\Py_Folder\yolo_obj_detection\yolo\yolov3.weights",
                      r"D:\NewFolder\Py_Folder\yolo_obj_detection\yolo\yolov3.cfg")

with open(r"D:\NewFolder\Py_Folder\yolo_obj_detection\yolo\coco.names", 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# 获取输出层信息
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

cap = cv2.VideoCapture(r"D:\A_Files_Saved\videos\road01.mp4")
# cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)

# 设置跳帧，来将视频播放速度和原视频对齐
# skip_frame = 2      # 这个参数指的每几帧挑一帧
# count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # count += 1
    # if count % skip_frame == 0:       # 跳帧
    #     continue

    height, width, channels = frame.shape
    # height,width = int(height / 2), int(width / 2)
    frame = cv2.resize(frame, (width, height))
    # 图像预处理
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
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
            confidence = scores[class_id]
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

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)    # 非极大值抑制

    font = cv2.FONT_HERSHEY_PLAIN   # 字体
    colors = np.random.uniform(0, 255, size=(len(classes), 3))  # 随机颜色

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label + " " + confidence, (x, y + 30), font, 2, color, 2)

    # cv2.imshow("Vid", frame)
    cv2.imshow("Vid_YOLO", frame)
    if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
