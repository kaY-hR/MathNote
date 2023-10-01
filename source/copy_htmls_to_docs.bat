@echo off
setlocal enabledelayedexpansion

REM 移動先フォルダのパス
set "destination=..\docs"

REM 移動先フォルダ内のファイルを削除
del /Q "!destination!\*.*"

REM カレントディレクトリ内のHTMLファイルをループ処理
for %%f in (*.html) do (
    REM コピー元のファイルパス
    set "source=%%~dpnxf"
    
    REM ファイルをコピー
    copy "!source!" "!destination!\%%~nxf"
)

REM コピー元のstyle.cssファイルパス
set "css_source=style.css"

REM コピー先のstyle.cssファイルパス
set "css_destination=!destination!\style.css"

REM style.cssファイルをコピー
if exist "!css_source!" (
    copy "!css_source!" "!css_destination!"
)

endlocal
