@echo off

chcp 65001

call venv\Scripts\activate
echo 已虛擬環境

start python main.py
echo 已啟動 main.py

echo 腳本執行完成