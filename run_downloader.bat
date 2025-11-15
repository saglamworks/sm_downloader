@echo off
REM ==========================
REM SM Downloader CLI Launcher
REM ==========================

REM Python scriptin bulunduğu klasöre geç
cd /d %~dp0

REM Python ile scripti çalıştır
python sm_downloader_cli.py

REM İşlem bittiğinde kullanıcı enter’a basana kadar bekle
pause
