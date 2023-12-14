#!/bin/bash

echo 正在建立虛擬環境
python -m venv venv
echo 已創建虛擬環境

source venv/bin/activate
echo 已啟動虛擬環境

pip install -r requirements.txt
echo 已安裝依賴環境