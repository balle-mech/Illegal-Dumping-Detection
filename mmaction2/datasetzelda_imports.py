# このサイトを参考にして、カスタムモジュールをインポートする
# https://mmengine.readthedocs.io/en/latest/advanced_tutorials/config.html#import-the-custom-module

datasetzelda_imports = dict(
    imports=['my_dataloader'], allow_failed_imports=False)

train_pipeline_cfg = [
    dict(type='VideoInit'),
    dict(type='VideoSample', clip_len=16, num_clips=1, test_mode=False),
    dict(type='VideoDecode'),
    dict(type='VideoResize', r_size=256),
    dict(type='VideoCrop', c_size=224),
    dict(type='VideoFormat'),
    dict(type='VideoPack')
]

train_dataset_cfg = dict(type='DatasetZelda',
                         ann_file='kinetics_tiny_train_video.txt', pipeline=train_pipeline_cfg, data_root='data/kinetics400_tiny/', data_prefix=dict(video='train'))
