import os

def create_markdown_table(base_folder):
    # 檢查基礎資料夾是否存在
    if not os.path.exists(base_folder):
        raise ValueError("指定的資料夾不存在")

    # 開始創建Markdown表格
    markdown_str = "| 子資料夾名稱 | 圖片 |\n"
    markdown_str += "| --- | --- |\n"

    for folder_name in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder_name)
        if os.path.isdir(folder_path):
            image_path = os.path.join(folder_name, 'sample.png')
            if os.path.exists(os.path.join(base_folder, image_path)):
                markdown_str += f"| {folder_name} | ![]({image_path}) |\n"
            else:
                markdown_str += f"| {folder_name} | 無圖片 |\n"

    # 寫入Markdown文件
    markdown_file_path = os.path.join(base_folder, 'folder_images.md')
    with open(markdown_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_str)

    print(f'Markdown 文件已保存在 {markdown_file_path}')

# 使用範例
base_folder = 'assets\category'
create_markdown_table(base_folder)

