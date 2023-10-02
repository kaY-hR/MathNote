import os
import argparse
from natsort import natsorted  # natsortをインポート

# コマンドライン引数の解析を設定
parser = argparse.ArgumentParser(description='Generate Markdown file for folder structure')
parser.add_argument('folder_path', type=str, help='Path to the folder structure')

# コマンドライン引数を解析
args = parser.parse_args()

# Markdownファイルを生成する再帰関数を定義
def generate_markdown(abs_path,folder_path, depth=0):
    folder_name = os.path.basename(folder_path)
    markdown = f"{'#' * (depth + 1)} {folder_name}\n\n"

    slide_names = []
    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)

        if os.path.isdir(item_path):
            markdown += generate_markdown(abs_path, item_path, depth + 1)
        else:
            slide_names.append(item_name)

    # スライド名を自然な順序でソート
    slide_names = natsorted(slide_names)

    # スライドへの画像リンクを追加
    for slide_name in slide_names:
        image_name = os.path.splitext(slide_name)[0]
        image_path = os.path.relpath(os.path.join(abs_path, folder_path, slide_name), args.folder_path)
        image_path = image_path.replace("\\","/")
        markdown += f"![{image_name}](/{image_path})\n"

    return markdown

# RootフォルダからMarkdownを生成
markdown_content = generate_markdown(args.folder_path,args.folder_path)


# template.mdの内容を読み取る
with open("resources/auto_pptx/template.md", "r", encoding="utf-8") as template_file:
    template_content = template_file.read()

# Markdownファイルを書き込み
markdown_file_name = f"{args.folder_path}.md"
with open(markdown_file_name, "w", encoding="utf-8") as markdown_file:
    markdown_file.write(template_content)
    markdown_file.write(markdown_content)

print(f"Markdownファイル '{markdown_file_name}' が生成されました。")
