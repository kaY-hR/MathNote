import os
import argparse

# コマンドライン引数の解析を設定
parser = argparse.ArgumentParser(description='Process subdirectory')
parser.add_argument('subdirectory', type=str, help='Subdirectory to process')

# コマンドライン引数を解析
args = parser.parse_args()

# ベースディレクトリのパスを指定します
base_directory = "resources/auto_pptx"

# template.mdの内容を読み取ります
with open("resources/auto_pptx/template.md", "r", encoding="utf-8") as template_file:
    template_content = template_file.read()

# サブディレクトリ内の画像ファイルの一覧を取得します
subdirectory_path = os.path.join(base_directory, args.subdirectory)
image_files = [f for f in os.listdir(subdirectory_path) if f.endswith(".JPG")]

# Markdownファイル名を生成します（例：プレゼン1.md）
markdown_file_name = f"source/{args.subdirectory}.md"

# MarkdownファイルをUTF-8エンコーディングで書き込みます
with open(markdown_file_name, "w", encoding="utf-8") as markdown_file:
    markdown_file.write(template_content+"\n\n")
    markdown_file.write("# "+args.subdirectory+"\n\n")
    # 画像ファイルをMarkdownに挿入します
    for i, image_file in enumerate(image_files, start=1):
        image_name = os.path.splitext(image_file)[0]
        image_path = os.path.join("../resources/auto_pptx", args.subdirectory, image_file)  # パスを修正
        image_path = image_path.replace("\\","/")
        markdown_file.write(f"![{image_name}]({image_path})\n")

print(f"Markdownファイル '{markdown_file_name}' が生成されました。")
