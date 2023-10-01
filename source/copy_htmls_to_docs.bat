@echo off
setlocal enabledelayedexpansion

REM カレントディレクトリ内のHTMLファイルをループ処理
for %%f in (*.html) do (
    REM コピー元のファイルパス
    set "source=%%~dpnxf"
    
    REM コピー先のフォルダパス
    set "destination=..\docs\%%~nxf"
    
    REM ファイルをコピー
    copy "!source!" "!destination!"
)

REM コピー元のstyle.cssファイルパス
set "css_source=style.css"

REM コピー先のstyle.cssファイルパス
set "css_destination=..\docs\style.css"

REM style.cssファイルをコピー
if exist "!css_source!" (
    copy "!css_source!" "!css_destination!"
)

endlocal
