@echo off
setlocal

REM コンパイルするファイル
set SOURCE_FILE=.\tools\ReviceMainHtml.cs

REM 出力ディレクトリ
set OUTPUT_DIR=.\tools\

REM csc.exeのパス
set CSC_PATH=C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe

REM csc.exeを使ってコンパイル
%csc_path% %SOURCE_FILE%

REM コンパイル結果を移動
move ReviceMainHtml.exe %OUTPUT_DIR%

echo 成果物を %OUTPUT_DIR% に移動しました。
pause
