#!/bin/bash

source venv/bin/activate
echo 已啟動虛擬環境

python main.py &
echo 已啟動main.py

echo 腳本執行完成