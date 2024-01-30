import os
# from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = '../.env'
load_dotenv(dotenv_path)

CUSTOM_DATA_PATH = os.environ.get('CUSTOM_DATA_PATH')
RASP_VIDEO_PATH = os.environ.get('RASP_VIDEO_PATH')
