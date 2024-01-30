# capture_video
import datetime
import picamera
import time
import config

RASP_VIDEO_PATH = config.RASP_VIDEO_PATH

current_time = datetime.datetime.now()
filename = '9_' + current_time.strftime("%m%d_%H%M") + '.h264'
video_path = RASP_VIDEO_PATH + filename

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)  # 解像度を設定
    camera.start_recording(video_path)  # h264形式で録画開始
    time.sleep(10)  # 10秒間録画
    camera.stop_recording()  # 録画停止
