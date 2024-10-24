import json

def setData(userid: str, updateData: dict):
    try:
        # 嘗試讀取舊有資料
        with open(f"data/{userid}.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        # 如果讀取失敗或文件不存在，初始化一個空字典
        data = {
            "id": userid,
            "money": 0
        }
    
    data.update(updateData)

    with open(f"data/{userid}.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def getData(userid: str):
    try:
        # 嘗試讀取舊有資料
        with open(f"data/{userid}.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        # 如果讀取失敗或文件不存在，初始化一個空字典
        data = {
            "id": 0,
            "money": 0
        }
    
    return data