import os
import json
import mmengine

# ファイルパスを指定
root_path = "./"
result_file_name = "val_10_pred.pkl"

# pickleファイルを読み込む
data_list = mmengine.load(os.path.join(root_path, result_file_name))

# 'pred_score', 'pred_label', 'gt_label'キーの値を抜き出して一つのリストにまとめる
extracted_data = [{'pred_score': item['pred_score'].tolist(), 'pred_label': item['pred_label'].tolist(
), 'gt_label': item['gt_label'].tolist()} for item in data_list]
print(extracted_data[0])

# JSONファイルに書き込む
pred_json_name = result_file_name.replace('.pkl', '.json')
pred_json_path = os.path.join(root_path, pred_json_name)
with open(pred_json_path, 'w') as f:
    json.dump(extracted_data, f)
