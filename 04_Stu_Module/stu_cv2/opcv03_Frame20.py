# 读取视频文件并每隔20帧保存一帧
import cv2
import os


def save_frames(video_path, output_folder):
    # 初始化帧计数器
    frame_count = 0
    video_capture = cv2.VideoCapture(video_path)

    while True:
        # 读取下一帧
        ret, frame = video_capture.read()
        if not ret:
            break
        # 每隔20帧保存
        frame_count += 1
        if frame_count % 20 == 0:
            # 构建保存的文件名，例如frame_0001.jpg, frame_0002.jpg等
            filename = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
            cv2.imwrite(filename, frame)
            print(f'Saved {filename}')

    # 释放视频捕获资源
    video_capture.release()
    print("Frame saving completed.")


video_file = r"D:\A_Files_Saved\ScreenRecord\VCR_1.mp4"  # 更换为你的视频文件路径
output_directory = 'D:\A_Files_Saved\py'  # 输出文件夹名称，确保此路径已存在
save_frames(video_file, output_directory)
