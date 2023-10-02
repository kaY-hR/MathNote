@echo off
setlocal enabledelayedexpansion

REM スクリプトのあるフォルダに移動
cd /d "%~dp0"

REM 移動先フォルダのパス
set "destination=..\docs"

REM 移動先フォルダ内のファイルを削除
del /Q "!destination!\*.*"

cd /d "..\source"
REM カレントディレクトリ内のHTMLファイルをループ処理
for %%f in (*.html) do (
    REM コピー元のファイルパス
    set "source=..\source\%%f"
    
    REM ファイルをコピー
    copy "!source!" "!destination!\%%f"
)

REM コピー元のstyle.cssファイルパス
set "css_source=..\source\style.css"

REM コピー先のstyle.cssファイルパス
set "css_destination=!destination!\style.css"

REM style.cssファイルをコピー
if exist "!css_source!" (
    copy "!css_source!" "!css_destination!"
)

REM assetsフォルダをコピー
xcopy /s /i "..\source\assets" "!destination!\assets"

endlocal
