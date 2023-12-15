import cv2

# カメラのキャプチャを開始
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラが見つかりません")
    exit()

img_count = 0

# メインループ
while True:
    # カメラからフレームを取得
    ret, frame = cap.read()

    # 取得したフレームを表示
    cv2.imshow('Press any key to capture', frame)

    # 任意のキー入力があるまで待つ
    key = cv2.waitKey(1)
    if key != -1:
        img_count += 1
        # 画像をPNG形式で保存
        img_name = f'  r{img_count}.png'
        cv2.imwrite(img_name, frame)
        print(f"Image saved as {img_name}!")

        # もし、'q' キーが押されたら終了
        if key == ord('q'):
            break

# カメラとウィンドウのリソースを解放
cap.release()
cv2.destroyAllWindows()
