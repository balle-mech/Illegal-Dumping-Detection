# capture_video.py
import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)  # 解像度を設定
    camera.start_recording('video.h264')  # h264形式で録画開始
    time.sleep(10)  # 10秒間録画
    camera.stop_recording()  # 録画停止
