import cv2
import numpy as np
import pickle
import os

# mp4ファイルを開く
cap = cv2.VideoCapture(
    '/Users/fukunagaatsushi/src/github.com/open-mmlab/mmaction2/demo/demo_configs/illegal.mp4')

frames = []

# フレームを読み込む
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    frames.append(frame)

cap.release()

# numpy配列に変換
frames_np = np.array(frames)

# pklファイルに保存
with open('output.pkl', 'wb') as f:
    pickle.dump(frames_np, f)
