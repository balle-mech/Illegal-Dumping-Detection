import pickle
import os

# その個数を辞書にまとめる
file_count_dict = {
    'dumping': 0,
    'walker': 0,
    'guard': 0
}

directory = './my_study/data/pkl_dataset/'

# ファイル名が'label_list'から始まるファイルの個数を数える
for i, file in enumerate(os.listdir(directory)):
    for key in file_count_dict.keys():
        if file.startswith(key):
            file_count_dict[key] += 1

# すべてのpickleファイルを読み込んでリストにまとめる
pickle_files = []

# すべてのpickleファイルのリストを作成する
for key, value in file_count_dict.items():
    for j in range(value):
        pickle_files.append(f'{key}_{j+1}.pkl')

data = []
for file in pickle_files:
    with open(directory+file, 'rb') as f:
        data.extend(pickle.load(f))

# まとめたリストを新しいpickleファイルとして保存する
output_file = './my_study/data/custom_dataset/custom_dataset_train.pkl'
with open(output_file, 'wb') as f:
    pickle.dump(data, f)
