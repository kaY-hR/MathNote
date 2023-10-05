# [こちらのサイト](https://kay-hr.github.io/NoteBook/)のソースです

私的な数学ノートです。  
同様の形式でノートを作りたいと思った方がいらっしゃれば、cloneして参考にしてください。

# ノートの作り方

1. Javaのインストール - plantuml用です。
1. VSCodeのインストール
    * 拡張機能 markdown preview enhanced のインストール
    * 拡張機能 plantuml のインストール
1. vscodeで最上階層を開く
1. ./source/{i}_Title.mdの形式でコンテンツページを作成
1. crtl+K -> VでPreview表示し、その状態でctrl+Sでmdファイルを保存
→htmlファイルが生成されます。
1. ./tools/ReviceMainHtml.exeを実行
1. ./source/index.htmlを開く

## 注意

* ここでは.vscode/settings.json内で、"markdown-preview-enhanced.enableScriptExecution": trueを設定しています。これはインデックスをサイドバーで表示するために必要ですが、セキュリティ上この設定が好ましくない場合は、削除またはfalseにしてください。
* copy_htmls_to_docs.batを実行すると、html/cssファイルがdocsフォルダにコピーされますが、これはGithub Pages用です。ローカルで使う場合はsourceフォルダのみを編集・閲覧するのみで十分です。

# その他使い方

## 親ページ(index.html)のスタイルを変更したいとき

style.cssを編集してください。

## 子ページのスタイルを変更したいとき

.crossnote内のstyle.lessを編集してください。

## markdownファイルを追加・削除したとき、またはタイトルを変更したとき

index.htmlを修正する必要があります。
ReviceMainHtml.exe を実行してください。

## ReviceMainHtml.csを修正したいとき

C#ソースをビルドするときは
<pre>C:\Windows\Microsoft.NET\Framework\\{ここは環境に依る}\csc.exe .\tools\ReviceMainHtml.cs</pre>

例:
<pre>C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe .\tools\ReviceMainHtml.cs</pre>

## pptxをmdに変換したいとき

1. pptxをresources/auto_pptxに配置し、pptxを開く
1. ファイル/エクスポート/ファイルの種類の変更/JPEGファイル交換形式 を選択し、同一フォルダ下に保存
1. resources/auto_pptx/{pptx名}フォルダが生成され、下に"スライド{i}.JPEG"が配置されていることを確認。
1. resources/auto_pptx/create_md_from_pptx.pyを実行する。
1. {200+i}_{pptx名}.mdが生成される。
