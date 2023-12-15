import cv2
import numpy as np
import tensorflow as tf

# TFLiteモデルのパス
# model_path = '/home/a2c6201/Illegal-Dumping-Detection/object_detection_mobile_object_localizer_v1_1_default_1.tflite'

# TensorFlow Liteモデルの読み込み
interpreter = tf.lite.Interpreter(model_path='/home/a2c6201/Illegal-Dumping-Detection/object_detection_mobile_object_localizer_v1_1_default_1.tflite')
interpreter.allocate_tensors()

# カメラの初期化
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # フレームをモデルの入力サイズにリサイズ
    input_tensor = interpreter.get_input_details()[0]['index']
    input_shape = interpreter.get_input_details()[0]['shape']
    resized_frame = cv2.resize(frame, (input_shape[1], input_shape[2]))
    input_data = np.expand_dims(resized_frame, axis=0)

    # 推論を実行
    interpreter.set_tensor(input_tensor, input_data)
    interpreter.invoke()

    # モデルの出力を取得
    output_tensor = interpreter.get_output_details()[0]['index']
    output_data = interpreter.get_tensor(output_tensor)

    # 人物が検出されたら、枠を描画
    if output_data[0][0] > 0.5:  # 0.5は適切な閾値
        cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 255, 0), 2)

    # フレームを表示
    cv2.imshow('Person Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
