import pandas as pd

# Excelファイルを読み込む
df = pd.read_excel('output.xlsx', sheet_name=0, header=None) # 'your_file.xlsx'をExcelファイルの実際のパスに置き換えてください

# 出力テキストを格納するためのリスト
events = []

# 1列目のすべての行に対して操作を行う
for tech in df[0]:
    # 文字列を作成
    event = f"\t\tgive_tech_no_error_effect = {{ MESSAGE = no TECH = {tech} }}"
    # イベントをリストに追加
    events.append(event)

# テキストファイルに保存
with open('events.txt', 'w') as f:
    for event in events:
        f.write("%s\n" % event)
