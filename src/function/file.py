import json
import os

def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            output_file = json.load(file)
            return output_file
    except FileNotFoundError:
        print(f"未找到原始文件 {file_path}。請確認文件是否存在。")
        return
    except json.JSONDecodeError:
        print(f"原始文件 {file_path} 格式錯誤。")
        return
    
def find_subdirectories(parent_directory):
    # 檢查給定的目錄是否真的存在
    if not os.path.exists(parent_directory):
        print("The specified directory does not exist")
        return []

    # 獲取所有子目錄和檔案
    entries = os.listdir(parent_directory)
    directories = []

    # 迴圈處理每一個項目，判斷是否為目錄
    for entry in entries:
        full_path = os.path.join(parent_directory, entry)
        if os.path.isdir(full_path):
            # 如果是目錄，則創建一個字典並添加到列表中
            directories.append({"name": entry, "path": full_path})

    return directories



