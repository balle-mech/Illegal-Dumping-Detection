import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CUSTOM_DATA_PATH = os.environ['CUSTOM_DATA_PATH']
RASP_VIDEO_PATH = os.environ['RASP_VIDEO_PATH']
