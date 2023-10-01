# 概要

Just Visit [Here](https://kay-hr.github.io/MathNote/)!

私的な数学ノートです。同様の形式でノートを作りたい方は、cloneして参考にしてください。

# ノートの作り方

1. Javaのインストール - plantuml用です。
1. VSCodeのインストール
    * 拡張機能 markdown preview enhanced のインストール
    * 拡張機能 plantuml のインストール
1. {i}_Title.mdの形式でコンテンツページを作成
1. crtl+K -> VでPreview表示し、その状態でctrl+Sでmdファイルを保存
→htmlファイルが生成されます。
1. ReviceMainHtml.exeを実行
1. 0_Main.htmlを開く

## 注意

ここでは.vscode/settings.json内で、"markdown-preview-enhanced.enableScriptExecution": trueを設定しています。これはインデックスをサイドバーで表示するために必要ですが、セキュリティ上この設定が好ましくない場合は、削除またはfalseにしてください。

# その他使い方

## 親ページ(0_Main.html)のスタイルを変更したいとき

style.cssを編集してください。

## 子ページのスタイルを変更したいとき

.crossnote内のstyle.lessを編集してください。

## markdownファイルを追加・削除したとき、またはタイトルを変更したとき

0_Main.htmlを修正する必要があります。
ReviceMainHtml.exe を実行してください。

## ReviceMainHtml.csを修正したいとき

C#ソースをビルドするときは
<pre>C:\Windows\Microsoft.NET\Framework\\{ここは環境に依る}\csc.exe .\ReviceMainHtml.cs</pre>

例:
<pre>C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe .\ReviceMainHtml.cs</pre>
