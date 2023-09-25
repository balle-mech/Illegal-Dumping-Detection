#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import time

import cv2

from yolox_onnx import YoloxONNX

# 検出閾値
score_th = 0.3

# カメラ準備
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

# モデルロード
yolox = YoloxONNX(
    model_path='yolox_nano.onnx',
    input_shape=(416, 416),
    class_score_th=0.3,
    nms_th=0.45,
    nms_score_th=0.1,
)

while True:
    start_time = time.time()

    # カメラキャプチャ
    ret, frame = cap.read()
    if not ret:
        break
    debug_image = copy.deepcopy(frame)

    # 推論実施
    bboxes, scores, class_ids = yolox.inference(frame)

    elapsed_time = time.time() - start_time

    # デバッグ描画
    for bbox, score, class_id in zip(bboxes, scores, class_ids):
        x1, y1, x2, y2 = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

        if score_th > score:
            continue

        # バウンディングボックス
        cv2.rectangle(debug_image, (x1, y1), (x2, y2), (0, 255, 0))

        # クラスID、スコア
        text = 'ID:' + str(int(class_id)) + '(' + '{:.2f}'.format(score) + ')'
        cv2.putText(debug_image, text, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))

    # 推論時間描画
    text = 'Elapsed time:' + '%.0f' % (elapsed_time * 1000)
    text = text + 'ms'
    cv2.putText(debug_image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 255, 0))

    # キー処理(ESC：終了)
    key = cv2.waitKey(1)
    if key == 27:  # ESC
        break

    # 画面反映
    cv2.imshow('YOLOX ONNX Sample', debug_image)

cap.release()
cv2.destroyAllWindows()
