import numpy as np
import cv2
import tflite_runtime.interpreter as tflite

# TFLiteモデルのパス
model_path = '/home/a2c6201/Illegal-Dumping-Detection/object_detection_mobile_object_localizer_v1_1_default_1.tflite'

# TFLiteインタープリタの初期化
interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# カメラの初期化
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    # フレームをリサイズしてモデルの入力サイズに合わせるなどの前処理を行う

    # モデルに入力を供給
    input_data = np.array(frame, dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # 推論を実行
    interpreter.invoke()

    # 出力を取得して解析
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # 出力を利用して物体認識の結果を描画するなどの後処理を行う

camera.release()
cv2.destroyAllWindows()
