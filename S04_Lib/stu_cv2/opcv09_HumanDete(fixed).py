import cv2
import os
import joblib
import time
import pandas as pd
import numpy as np

height_compressed = 640
width_compressed = 360
path = "D:/NewFolder/ObjectDetection_YF/videos/"
path_models = "D:/NewFolder/ObjectDetection_YF/models/"
file_list = os.listdir(path_models)
print(file_list)

clf = joblib.load(path_models+'clf_adaboost.m')   # 加载模型

cap = cv2.VideoCapture(path+'test.mp4')
n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))   # 获取视频的帧数
print('视频文件的帧数量为：', n_frames)
fps = cap.get(cv2.CAP_PROP_FPS)
print('视频文件的帧率为：', fps)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('视频文件帧的宽度和高度分别为：', size)
# 定义编解码器并创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('D:/ai_sensing/videos/man_detection.mp4', fourcc, fps,
#                       (width_compressed, height_compressed))
count = 0
start = time.time()     # 计时，起始时间
while cap.isOpened():
    ret, frame0 = cap.read()
    if ret:
        # frame0 = np.rot90(frame0, -1)
        frame0 = cv2.resize(frame0, (width_compressed,height_compressed))#压缩
        frame = frame0[0:, 0:, :]   # 用于改变帧，测试算法的性能
        seg_h, seg_w = 300, 100
        n_step = 5  # 窗口横向、纵向等分的数量，决定重叠率，值越大，重叠率越高
        n_win_w = int(n_step*width_compressed/seg_w)    # 横向窗口数量，保持(n_step-1)/n_step的重叠率
        n_win_h = int(n_step*height_compressed/seg_h)   # 纵向窗口数量，保持(n_step-1)/n_step的重叠率
        step_w, step_h = int(seg_w/n_step),int(seg_h/n_step)  # 窗口横、纵向移动步长
        pos_w, pos_h = [], []
        for n_h in range(n_win_h):
            for n_w in range(n_win_w):
                # 视频帧采样
                sample_frame = frame[n_h*step_h:n_h*step_h+seg_h,
                             n_w * step_w:n_w*step_w+seg_w]
                if sample_frame.shape[0] >= seg_h and sample_frame.shape[1] >= seg_w:
                    sample_frame = cv2.resize(sample_frame, (10, 30))   # 宽，高
                    sample_frame = cv2.cvtColor(sample_frame, cv2.COLOR_BGR2GRAY)
                    X = sample_frame.reshape(1,-1)
                    y = clf.predict(X)
                    # 获取有人区域的切片位置
                    if y[0]=='man':
                        pos_w.append(n_w*step_w)
                        pos_h.append(n_h*step_h)
        print('检测到的有人区域数量为：', len(pos_w))
        tun_left_w, tun_top_h = 0, 0
        if len(pos_w) == 0 or len(pos_h) == 0:  # 如果没有检测到人区域
            pass
        else:
            # 求取同一帧上多个被预测为有人区域的切片平均位置
            tun_left_w = int(np.mean(pos_w))
            tun_top_h = int(np.mean(pos_h))
        adjust_w, adjust_h = 0, 0   # 修正
        # 绘制矩形，包围人区域。矩形坐标：左上，右下
        cv2.rectangle(frame, (tun_left_w+adjust_w, tun_top_h+adjust_h),
                      (tun_left_w+adjust_w+seg_w, tun_top_h+adjust_h+seg_h), (255, 0, 0), 3)    # 画矩形
        # out.write(frame)
        cv2.imshow('myvideo', frame)
        if count % 10 == 0:
            current = time.time()
            print('当前处理第', count, '帧， ', "用时：{:.2f}秒".format(current - start))
            count += 1
        key = (cv2.waitKey(100) & 0xFF)
        if key == 27:  # 按esc键退出
            break
    else:
        break
end = time.time()
print("用时：{:.2f}秒".format(end - start))
cap.release()
# out.release()
cv2.destroyAllWindows()
