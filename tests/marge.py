import os

def merge_program_files(source_folder, target_file, file_extension):
    """
    將特定資料夾下的所有指定擴展名的程式檔案內容整合到一個檔案中。

    :param source_folder: 包含源程式檔案的資料夾路徑
    :param target_file: 要將所有程式內容整合進的目標檔案路徑
    :param file_extension: 需要整合的檔案擴展名（如'.py', '.java'）
    """
    with open(target_file, 'w', encoding='utf-8') as outfile:
        # 遍歷資料夾
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                # 檢查檔案是否是指定的擴展名
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    # 讀取檔案並寫入目標檔案
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        contents = infile.read()
                        outfile.write(f"// File: {file}\n")
                        outfile.write(contents)
                        outfile.write("\n\n")  # 在檔案內容間加入空行以便於區分

# 使用範例
merge_program_files("D:\Programming\Python\\20240408_Project_Asur\Project_Asur\src", "merged_programs.txt", ".py")
