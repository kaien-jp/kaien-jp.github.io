# -*- coding: utf-8 -*-

import csv
from jinja2 import Environment, FileSystemLoader

csv_file = 'data_with_headings.csv'
output_html_file = 'output.html'

# Jinja2環境の設定
# テンプレートファイルがあるディレクトリを指定
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('mental_care_prompt_template.html')

# CSVファイルを読み込む
def read_csv(file_path):
    data = {}
    with open(file_path, 'r', encoding='cp932') as f:
        reader = csv.DictReader(f)
        for row in reader:
            l = []
            if row['カテゴリ'] in data:
                l = data[row['カテゴリ']]
            else:
                data[row['カテゴリ']] = l
            l.append(row)
    return data

# メイン処理
if __name__ == "__main__":
    try:
        # CSVからデータを取得
        csv_data = read_csv(csv_file)

        # テンプレートにデータを渡し、HTMLをレンダリング
        rendered_html = template.render(data=csv_data)
        
        # 結果をHTMLファイルに書き出す
        with open(output_html_file, 'w', encoding='utf-8') as f:
            f.write(rendered_html)
            
        print(f"HTMLファイル '{output_html_file}' が正常に生成されました。")
        
    except FileNotFoundError:
        print(f"エラー: '{csv_file}' または 'mental_care_prompt_template.html' が見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
