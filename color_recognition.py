import numpy as np
import tflite_runtime.interpreter as tflite
import glob
import cv2
#X_test = []
#y_test = []

# TensorFlow Liteモデルをロード
interpreter = tflite.Interpreter(model_path="/home/a2c6201/Illegal-Dumping-Detection/object_detection_mobile_object_localizer_v1_1_default_1.tflite")
interpreter.allocate_tensors()

# モデルの入力テンソル情報を取得
input_details = interpreter.get_input_details()
# 入力テンソルの形状情報からバッチサイズを取得
batch_size_model = input_details[0]['shape'][0]
print("モデルのバッチサイズ:", batch_size_model)

# 入力テンソルの形状情報を表示
for detail in input_details:
    print("Input name:", detail["name"])
    print("Input shape:", detail["shape"])
    print("Input data type:", detail["dtype"])
    print("Input quantization (if applicable):", detail.get("quantization", "None"))

# 画像データのパスを取得
#image_paths = glob.glob("/home/pi2023/Desktop/image/test/0_red/red1.png")
#image_paths = glob.glob("/home/pi2023/Desktop/image/test/1_blue/blue1.png")
#image_paths = glob.glob("/home/pi2023/Desktop/image/test/2_yellow/yellow1.png")
image_paths = glob.glob("/home/pi2023/Desktop/image/test/3_green/green1.png")
batch_size = 1

print("Image_pathsは")
print(image_paths)

interpreter = tflite.Interpreter(model_path="/home/a2c6201/Illegal-Dumping-Detection/object_detection_mobile_object_localizer_v1_1_default_1.tflite")
interpreter.allocate_tensors()
print("interpreterは")
print(interpreter)


# 画像データを読み込み、データ拡張を行う関数を定義
def load_and_preprocess_image(image_path):
# 画像ファイルの読み込み
    img_data = cv2.imread(image_path)#.astype(np.float32)
 # 画像を指定のサイズにリサイズ
    img_data = cv2.resize(img_data, (640, 480))
# 画像をTensorFlow Liteモデルに供給できる形式に変換（例えば正規化）
    img_data = img_data.astype(np.float32) / 255.0  #モデル正規化してたっけ？してないよね？
    
    # データのデータ型を確認
    data_type = img_data.dtype
    print("データのデータ型:", data_type)
    
    # データのバッチサイズを確認
    batch_size_data = img_data.shape

    print("データのバッチサイズ:", batch_size_data) #3次元になっているからバッチがない状態
    
    return img_data

#images = [load_and_preprocess_image(f) for f in image_paths]

# print(images) #kakuninn



# バッチを作成して4次元のテンソルに変換
batched_images = []
#current_batch = []

for image_path in image_paths:
    img = load_and_preprocess_image(image_path)
    batched_images.append(img)

    #if len(current_batch) == batch_size:
        #batched_images.append(current_batch)
        #current_batch = []

# 最後のバッチを追加（バッチサイズに満たない場合）
#if current_batch:
    #batched_images.append(current_batch)

# 4次元のテンソルに変換
batched_images = np.array(batched_images)

# モデルの入力テンソルの形状を確認
#input_details = interpreter.get_input_details()
#expected_input_shape = input_details[0]['shape']
#print("Expected Input Shape:", expected_input_shape)

# バッチ数と各バッチの形状を確認
#print("バッチ数:", len(batched_images))
#for i, batch in enumerate(batched_images):
 #   print(f"バッチ {i+1} の形状:", batch.shape)


# バッチサイズを正しく設定
input_details[0]['shape'] = (1, 480, 640, 3)#batched_images.shape[0]#expected_input_shape[0] = batched_images.shape[0]

# 入力テンソルにデータを設定
interpreter.set_tensor(input_details[0]['index'], batched_images)

# モデルの入力と出力のテンソルを取得
#input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 画像データをモデルの入力テンソルに設定
#interpreter.set_tensor(input_details[0]['index'], images[0])  # 例: 最初の画像を設定

# 推論を実行
interpreter.invoke()

# 推論結果を取得
output_data = interpreter.get_tensor(output_details[0]['index'])

print(output_data)

# モデルの出力（例: 推論結果）
output_data = np.array([output_data])
# クラスのリスト
class_names = ["Class_0", " y", "blue", "green","w","bk"]
# 最も高い確率を持つクラスのインデックスを取得
predicted_class_index = np.argmax(output_data)
# 予測されたクラス名を取得
predicted_class_name = class_names[predicted_class_index]
print("Predicted Class:", predicted_class_name)

# カメラ

import time

cap = cv2.VideoCapture(0)  # 0はカメラのデバイス番号

while True:
    ret, frame = cap.read()  # フレームを取得
    if not ret:
        print("Failed to grab frame")
        break

    # 画像を前処理
    frame_resized = cv2.resize(frame, (640, 480))
    frame_normalized = frame_resized.astype(np.float32) / 255.0
    frame_expanded = np.expand_dims(frame_normalized, axis=0)

    # モデルにフレームを供給して推論
    interpreter.set_tensor(input_details[0]['index'], frame_expanded)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_class_index = np.argmax(output_data)
    predicted_class_name = class_names[predicted_class_index]

    # 結果を表示
    label = "Predicted Class: " + predicted_class_name
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Real-time Image Recognition", frame)

    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.05)  # 50msウェイト

cap.release()
cv2.destroyAllWindows()
import numpy as np
import tflite_runtime.interpreter as tflite
import glob
import cv2
#X_test = []
#y_test = []

# TensorFlow Liteモデルをロード
interpreter = tflite.Interpreter(model_path="/home/pi2023/Desktop/my_model.tflite_3")
interpreter.allocate_tensors()

# モデルの入力テンソル情報を取得
input_details = interpreter.get_input_details()
# 入力テンソルの形状情報からバッチサイズを取得
batch_size_model = input_details[0]['shape'][0]
print("モデルのバッチサイズ:", batch_size_model)

# 入力テンソルの形状情報を表示
for detail in input_details:
    print("Input name:", detail["name"])
    print("Input shape:", detail["shape"])
    print("Input data type:", detail["dtype"])
    print("Input quantization (if applicable):", detail.get("quantization", "None"))

# 画像データのパスを取得
#image_paths = glob.glob("/home/pi2023/Desktop/image/test/0_red/red1.png")
#image_paths = glob.glob("/home/pi2023/Desktop/image/test/1_blue/blue1.png")
#image_paths = glob.glob("/home/pi2023/Desktop/image/test/2_yellow/yellow1.png")
image_paths = glob.glob("/home/pi2023/Desktop/image/test/3_green/green1.png")
batch_size = 1

print("Image_pathsは")
print(image_paths)

interpreter = tflite.Interpreter(model_path="/home/pi2023/Desktop/my_model.tflite_3")
interpreter.allocate_tensors()
print("interpreterは")
print(interpreter)


# 画像データを読み込み、データ拡張を行う関数を定義
def load_and_preprocess_image(image_path):
# 画像ファイルの読み込み
    img_data = cv2.imread(image_path)#.astype(np.float32)
 # 画像を指定のサイズにリサイズ
    img_data = cv2.resize(img_data, (640, 480))
# 画像をTensorFlow Liteモデルに供給できる形式に変換（例えば正規化）
    img_data = img_data.astype(np.float32) / 255.0  #モデル正規化してたっけ？してないよね？
    
    # データのデータ型を確認
    data_type = img_data.dtype
    print("データのデータ型:", data_type)
    
    # データのバッチサイズを確認
    batch_size_data = img_data.shape

    print("データのバッチサイズ:", batch_size_data) #3次元になっているからバッチがない状態
    
    return img_data

#images = [load_and_preprocess_image(f) for f in image_paths]

# print(images) #kakuninn



# バッチを作成して4次元のテンソルに変換
batched_images = []
#current_batch = []

for image_path in image_paths:
    img = load_and_preprocess_image(image_path)
    batched_images.append(img)

    #if len(current_batch) == batch_size:
        #batched_images.append(current_batch)
        #current_batch = []

# 最後のバッチを追加（バッチサイズに満たない場合）
#if current_batch:
    #batched_images.append(current_batch)

# 4次元のテンソルに変換
batched_images = np.array(batched_images)

# モデルの入力テンソルの形状を確認
#input_details = interpreter.get_input_details()
#expected_input_shape = input_details[0]['shape']
#print("Expected Input Shape:", expected_input_shape)

# バッチ数と各バッチの形状を確認
#print("バッチ数:", len(batched_images))
#for i, batch in enumerate(batched_images):
 #   print(f"バッチ {i+1} の形状:", batch.shape)


# バッチサイズを正しく設定
input_details[0]['shape'] = (1, 480, 640, 3)#batched_images.shape[0]#expected_input_shape[0] = batched_images.shape[0]

# 入力テンソルにデータを設定
interpreter.set_tensor(input_details[0]['index'], batched_images)

# モデルの入力と出力のテンソルを取得
#input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 画像データをモデルの入力テンソルに設定
#interpreter.set_tensor(input_details[0]['index'], images[0])  # 例: 最初の画像を設定

# 推論を実行
interpreter.invoke()

# 推論結果を取得
output_data = interpreter.get_tensor(output_details[0]['index'])

print(output_data)

# モデルの出力（例: 推論結果）
output_data = np.array([output_data])
# クラスのリスト
class_names = ["Class_0", " y", "blue", "green","w","bk"]
# 最も高い確率を持つクラスのインデックスを取得
predicted_class_index = np.argmax(output_data)
# 予測されたクラス名を取得
predicted_class_name = class_names[predicted_class_index]
print("Predicted Class:", predicted_class_name)

# カメラ

import time

cap = cv2.VideoCapture(0)  # 0はカメラのデバイス番号

while True:
    ret, frame = cap.read()  # フレームを取得
    if not ret:
        print("Failed to grab frame")
        break

    # 画像を前処理
    frame_resized = cv2.resize(frame, (640, 480))
    frame_normalized = frame_resized.astype(np.float32) / 255.0
    frame_expanded = np.expand_dims(frame_normalized, axis=0)

    # モデルにフレームを供給して推論
    interpreter.set_tensor(input_details[0]['index'], frame_expanded)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_class_index = np.argmax(output_data)
    predicted_class_name = class_names[predicted_class_index]

    # 結果を表示
    label = "Predicted Class: " + predicted_class_name
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Real-time Image Recognition", frame)

    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.05)  # 50msウェイト

cap.release()
cv2.destroyAllWindows()
