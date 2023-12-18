# from mmaction.datasets.my_dataset import DatasetZelda
from mmaction.registry import MODELS
from mmengine.runner import Runner
from mmaction.registry import DATASETS
import torch
from mmaction.datasets.my_dataset import DatasetZelda
from mmengine.config import Config

# DATASETをカスタマイズして、DatasetZeldaを登録する
# OPTIMIZERSがDATASET
# CustomOptim=DatasetZelda
DATASETS.register_module(name='DatasetZelda', module=DatasetZelda, force=True)

train_pipeline_cfg = [
    dict(type='VideoInit'),
    dict(type='VideoSample', clip_len=16, num_clips=1, test_mode=False),
    dict(type='VideoDecode'),
    dict(type='VideoResize', r_size=256),
    dict(type='VideoCrop', c_size=224),
    dict(type='VideoFormat'),
    dict(type='VideoPack')
]

val_pipeline_cfg = [
    dict(type='VideoInit'),
    dict(type='VideoSample', clip_len=16, num_clips=5, test_mode=True),
    dict(type='VideoDecode'),
    dict(type='VideoResize', r_size=256),
    dict(type='VideoCrop', c_size=224),
    dict(type='VideoFormat'),
    dict(type='VideoPack')
]

train_dataset_cfg = dict(
    type='DatasetZelda',
    ann_file='kinetics_tiny_train_video.txt',
    pipeline=train_pipeline_cfg,
    data_root='data/kinetics400_tiny/',
    data_prefix=dict(video='train'))

# 公式を参考にして、Configを使ってDatasetZeldaを作成する
cfg = Config.fromfile('datasetzelda_imports.py')
train_dataset = DATASETS.build(cfg.train_dataset_cfg)
print('DatasetZelda object:', train_dataset)  # DatasetZelda object
print('------------------')

val_dataset_cfg = dict(
    type='DatasetZelda',
    ann_file='kinetics_tiny_val_video.txt',
    pipeline=val_pipeline_cfg,
    data_root='data/kinetics400_tiny/',
    data_prefix=dict(video='val'))

# train_dataset = DATASETS.build(train_dataset_cfg)

packed_results = train_dataset[0]

inputs = packed_results['inputs']
data_sample = packed_results['data_samples']

print('shape of the inputs: ', inputs.shape)

# 入力のメタ情報を取得する
print('image_shape: ', data_sample.img_shape)
print('num_clips: ', data_sample.num_clips)
print('clip_len: ', data_sample.clip_len)

# 入力のラベルを取得する
print('label: ', data_sample.gt_label)
print('------------------')


BATCH_SIZE = 2

train_dataloader_cfg = dict(
    batch_size=BATCH_SIZE,
    num_workers=0,
    persistent_workers=False,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=train_dataset_cfg)

val_dataloader_cfg = dict(
    batch_size=BATCH_SIZE,
    num_workers=0,
    persistent_workers=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=val_dataset_cfg)

train_data_loader = Runner.build_dataloader(dataloader=train_dataloader_cfg)
val_data_loader = Runner.build_dataloader(dataloader=val_dataloader_cfg)

batched_packed_results = next(iter(train_data_loader))

batched_inputs = batched_packed_results['inputs']
batched_data_sample = batched_packed_results['data_samples']

assert len(batched_inputs) == BATCH_SIZE
assert len(batched_data_sample) == BATCH_SIZE


# data_loaderの出力を確認する
data_preprocessor_cfg = dict(
    type='DataPreprocessorZelda',
    mean=[123.675, 116.28, 103.53],
    std=[58.395, 57.12, 57.375])

data_preprocessor = MODELS.build(data_preprocessor_cfg)

preprocessed_inputs = data_preprocessor(batched_packed_results)
print('preprocessed_inputs.shape: ', preprocessed_inputs['inputs'].shape)

torch.Size([2, 1, 3, 16, 224, 224])
