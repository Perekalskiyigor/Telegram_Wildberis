@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5947542394:AAGKFymHjLa--3bMz2QF8q-CP-EgfdWyKEE
python bot.py

pause