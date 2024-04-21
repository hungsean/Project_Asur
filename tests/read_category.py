import os

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

# 使用函數
parent_dir = "assets\category"  # 這裡替換成你的目錄路徑
subdirectories = find_subdirectories(parent_dir)
print(subdirectories)
