@echo off

chcp 65001

call venv\Scripts\activate
echo 已啟動虛擬環境

start python main.py
echo 已啟動main.py

echo 腳本執行完成