'''这个程序会保存视频帧到本地！不要随便运行！！！'''
# 对原始视频的每一帧，压缩到指定大小。使用窗口自左至右、自上向下滑动采样，获取每帧的许多切片
import pandas as pd
import os
import cv2
import numpy as np

height_compressed = 640  # 帧压缩的高度
width_compressed = 360  # 帧压缩的宽度
path = "D:/NewFolder/ObjectDetection_YF/videos/"
path_frame = "D:/NewFolder/ObjectDetection_YF/seg_frames/"

cap = cv2.VideoCapture(path + "man.mp4")
n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('视频文件的帧数量为：', n_frames)
fps = cap.get(cv2.CAP_PROP_FPS)
print('视频文件的帧率为：', fps)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('视频文件帧的宽度和高度分别为：', size)

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # frame=np.rot90(frame,-1)      # 如果读取的视频帧方向不正确，则需将其旋转90度的整数倍
        frame = cv2.resize(frame, (width_compressed, height_compressed))  # 压缩帧
        seg_h, seg_w = 300, 100  # 采样窗口大小
        n_step = 5  # 采样窗口的横、纵向等分数量
        n_win_w = int(n_step * width_compressed / seg_w)  # 横向窗口数量，保持(n_step-1)/n_step的重叠率
        n_win_h = int(n_step * height_compressed / seg_h)  # 纵向窗口数量，保持(n_step-1)/n_step的重叠率
        # 以采样窗口的横、纵向各n_step等分作为各自的移动步长
        step_w, step_h = int(seg_w / n_step), int(seg_h / n_step)
        count2 = 0
        for n_h in range(n_win_h):
            for n_w in range(n_win_w):
                sample_frame = frame[n_h * step_h:n_h * step_h + seg_h, n_w * step_w:n_w * step_w + seg_w]
                # 确保采样切片与窗口大小相同
                if sample_frame.shape[0] >= seg_h and sample_frame.shape[1] >= seg_w:
                    cv2.imwrite(path_frame + str(count).zfill(10) + str(count2).zfill(5) + '.jpg', sample_frame)
                    count2 += 1
        cv2.imshow('MyVideo', cv2.resize(frame, (width_compressed, height_compressed)))
        count += 1
        key = cv2.waitKey(25) & 0xFF
        if key == 27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

source_file_list = os.listdir(path_frame)
print('获得的切片数量为：', len(source_file_list))
for file_name in source_file_list[0:]:  # 遍历源某类别目录下的所有文件
    # 拼出文件名全路径
    fullname = path_frame + file_name
    img0 = cv2.imread(fullname)

# 人工选择将获取的视频帧切片标注为有人、无人两个类别，分别存放后，分类别逐张读取图像，压缩，转灰度，保存为csv文件
import time
import matplotlib.pyplot as plt
# 保存标注图片的子文件夹所在位置
path2 = r"D:/NewFolder/ObjectDetection_YF/frames/"
source_category_list = os.listdir(path2)
print('original目录下的子目录为：\n', source_category_list)

# 分类别读取原始图片，压缩，保存为csv
X = []  # 保存特征集的列表
y = []  # 保存目标集的列表
print('图像文件批量压缩进行中，请耐心等待......')
for mydir in source_category_list:
    source_category_path = path2 + mydir + "/"
    # 获取某一目录（类别）中的所有原始文件
    source_file_list = os.listdir(source_category_path)
    file_num = len(source_file_list)  # 获取source_file_list文件数量
    for file_name, file_idx in zip(source_file_list, range(file_num)):  # 遍历源某类别目录下的所有文
        fullname = source_category_path + file_name
        img0 = cv2.imread(source_category_path + file_name)
        img_resized = cv2.resize(img0, (10, 30))  # 压缩图像，(宽，高)
        img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)  # 转灰度图像
        X = np.append(X, img_gray.ravel())
        y = np.append(y, mydir)
print('图像文件批量压缩完毕！')
X = np.array(X)
X = X.reshape(len(y), -1)
print('数据集的形状为：', X.shape)
print('目标集的形状为：', y.shape)

path3 = "D:/NewFolder/ObjectDetection_YF/data/"
if not os.path.exists(path3):
    os.makedirs(path3)
df_images_data = pd.DataFrame(X)
df_images_data.to_csv(path3 + 'my_data.csv', sep=',', index=False)  # 保存为csv文本文件
df_images_target = pd.DataFrame(y)
df_images_target.to_csv(path3 + 'my_target.csv', sep=',', index=False)  # 保存为csv文本文件
print('图像数据集转换为DataFrame并保存完毕！')

X1 = pd.read_table(path3 + 'my_data.csv', sep=',', encoding='gbk').values
y1 = pd.read_table(path3 + 'my_target.csv', sep=',', encoding='gbk').values
print('读取的图像数据文件特征集形状为：', X1.shape)
print('读取的图像数据文件目标集形状为：', y1.shape)

idx = np.random.randint(0, high=len(y1), size=50)
print('读取的图像数据文件中任意50个样本的的图像为：\n')
p = plt.figure(figsize=(10, 6))
for fignum in range(len(idx)):
    ax1 = p.add_subplot(5, 10, fignum + 1)
    # 恢复为压缩图像的形状（64,36）
    plt.imshow(X1[idx[fignum], :].reshape(30, 10), cmap='gray')
    p.tight_layout()  # 调整空白，避免子图重叠

# 读取图像数据集文本文件，训练分类器，实验SVM分类
path = "D:/NewFolder/ObjectDetection_YF/data/"
# 读取保存的图像数据集文件
X = pd.read_table(path+'my_data.csv', sep=',', encoding='gbk').values   # 读取csv文本文件
y = pd.read_table(path+'my_target.csv', sep=',', encoding='gbk').values   # 读取csv文本文件
print('读取的图像数据文件特征集形状为：', X.shape)
print('读取的图像数据文件目标集形状为：', y.shape)

# 观察任意50个样本
idx2 = np.random.randint(0, high=len(y), size=50)
print('读取的图像数据文件中任意50个样本的的图像为：\n')
p = plt.figure(figsize=(10, 6))
for fignum in range(len(idx2)):
    ax1 = p.add_subplot(5, 10, fignum+1)
    # 恢复为压缩图像的形状（64,36）
    plt.imshow(X[idx2[fignum], :].reshape(30, 10), cmap='gray')
    p.tight_layout()    # 调整空白，避免子图重叠
plt.show()


# 训练支持向量机分类器
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, test_size=0.3, random_state=42)
# 使用支持向量机进行训练
# 可选择不同的核函数kernel： 'linear', 'poly', 'rbf','sigmoid'
clf_svm = svm.SVC(kernel='linear', gamma=2)  # 设置模型参数
clf_svm.fit(X_train, y_train.ravel())  # 训练
y_svm_pred = clf_svm.predict(X_test)
print('支持向量机预测测试集结果与实际结果的混淆矩阵为：\n',
      confusion_matrix(y_test.ravel(), y_svm_pred.ravel()))  # 输出混淆矩阵
print('支持向量机预测结果评价报告：\n', classification_report(y_test.ravel(), y_svm_pred.ravel()))
# 交叉检验
print('交叉检验的结果为：',cross_val_score(clf_svm, X, y.ravel(), cv=5))


# 保存训练的支持向量机分类模型
import joblib
path_models = "D:/NewFolder/ObjectDetection_YF/models/"

if not os.path.exists(path_models):
    os.makedirs(path_models)
joblib.dump(clf_svm, path_models+'clf_svm.m')    # 保存模型
print('svm模型保存完毕！\n')

# 训练决策树分类器
from sklearn import tree
# 调用决策树分类器，添加参数
clf_tree = tree.DecisionTreeClassifier(criterion='entropy',max_depth=5)
# 将训练集和目标集进行匹配训练
clf_tree.fit(X_train, y_train.ravel())  # 训练
y_tree_pred = clf_tree.predict(X_test)
print('混淆矩阵为：\n', confusion_matrix(y_test.ravel(), y_tree_pred.ravel()))    # 输出混淆矩阵
print('结果评价报告：\n', classification_report(y_test.ravel(), y_tree_pred.ravel()))
print('交叉检验的结果为：', cross_val_score(clf_tree, X, y.ravel(), cv=5))
joblib.dump(clf_tree, path_models+'clf_tree.m')     # 保存模型
print('tree模型保存完毕！\n')

# 训练随机森林（RF）分类器
from sklearn.ensemble import RandomForestClassifier
clf_rfc = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=5, random_state=0)
clf_rfc.fit(X_train, y_train.ravel())
y_rfc_pred = clf_rfc.predict(X_test)
print('混淆矩阵为：\n', confusion_matrix(y_test.ravel(), y_rfc_pred.ravel()))    # 输出混淆矩阵
print('结果评价报告：\n', classification_report(y_test.ravel(), y_rfc_pred.ravel()))
print('交叉检验的结果为：', cross_val_score(clf_rfc, X, y.ravel(), cv=5))
joblib.dump(clf_rfc, path_models+'clf_rforest.m')   # 保存模型
print('rforset模型保存完毕！\n')

# 训练Bagging（装袋算法）分类器
from sklearn.ensemble import BaggingClassifier
clf_bagging = BaggingClassifier(svm.SVC(kernel='linear',gamma=2),n_estimators=6)
clf_bagging.fit(X_train, y_train.ravel())
y_bag_pred = clf_bagging.predict(X_test)
print('混淆矩阵为：\n', confusion_matrix(y_test.ravel(), y_bag_pred.ravel()))     # 输出混淆矩阵
print('结果评价报告：\n', classification_report(y_test.ravel(),y_bag_pred.ravel()))
# 交叉检验
print('交叉检验的结果为：', cross_val_score(clf_bagging, X, y.ravel(), cv=5))
# 保存训练的分类模型
joblib.dump(clf_bagging,path_models+'clf_bagging.m')    # 保存模型
print('bagging模型保存完毕！\n')

# 训练gboost（梯度提升树）分类器
from sklearn.ensemble import GradientBoostingClassifier
clf_gboost = GradientBoostingClassifier()   # 设置模型参数
import datetime
start_time = datetime.datetime.now()
clf_gboost.fit(X_train,y_train.ravel())
now_time = datetime.datetime.now()
print('模型训练用时：', now_time-start_time)
y_gboost_pred = clf_gboost.predict(X_test)
print('混淆矩阵为：\n', confusion_matrix(y_test.ravel(), y_gboost_pred.ravel()))   # 输出混淆矩阵
print('结果评价报告：\n', classification_report(y_test.ravel(), y_gboost_pred.ravel()))
# 交叉检验
print('交叉检验的结果为：', cross_val_score(clf_gboost, X, y.ravel(), cv=5))
joblib.dump(clf_gboost,path_models+'clf_gboost.m')  # 保存模型
print('gboost模型保存完毕！\n')

# 训练adaboost（自适应增强）分类器
from sklearn.ensemble import AdaBoostClassifier
clf_adaboost = AdaBoostClassifier()  # 设置
start_time = datetime.datetime.now()
clf_adaboost.fit(X_train,y_train)
now_time = datetime.datetime.now()
print('模型训练用时：', now_time-start_time)
y_adaboost_pred = clf_adaboost.predict(X_test)
print('混淆矩阵为：\n', confusion_matrix(y_test.ravel(), y_adaboost_pred.ravel()))    # 输出混淆矩阵
print('结果评价报告：\n', classification_report(y_test.ravel(), y_adaboost_pred.ravel()))
# 交叉检验
print('交叉检验的结果为：', cross_val_score(clf_adaboost, X, y.ravel(), cv=5))
joblib.dump(clf_adaboost, path_models+'clf_adaboost.m')      # 保存模型
print('adaboost模型保存完毕！')
