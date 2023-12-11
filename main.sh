#!/bin/bash

echo "正在載入虛擬環境..."
source venv/bin/activate

echo "啟動主程式..."
python main.py &

echo "啟動完成"
