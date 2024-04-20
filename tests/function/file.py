import json

def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            output_file = json.load(file)
            return output_file
    except FileNotFoundError:
        print("未找到原始文件 'rectangles.json'。請確認文件是否存在。")
        return
    except json.JSONDecodeError:
        print("原始文件 'rectangles.json' 格式錯誤。")
        return

