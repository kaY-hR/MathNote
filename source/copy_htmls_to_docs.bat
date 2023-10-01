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

endlocal
