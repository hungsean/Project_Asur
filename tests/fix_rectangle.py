import json
import datetime

def resize_coordinates():
    # 讀取原始矩形數據
    try:
        with open('garbage\\20240422192944.json', 'r', encoding='utf-8') as file:
            rectangles = json.load(file)
    except FileNotFoundError:
        print("未找到原始文件 'rectangles.json'。請確認文件是否存在。")
        return
    except json.JSONDecodeError:
        print("原始文件 'rectangles.json' 格式錯誤。")
        return

    # 縮放比例
    x_scale = 1280 / 1920
    y_scale = 720 / 1080

    # 轉換座標
    resized_rectangles = []
    count = 0
    for rect in rectangles:
        start_x = int(rect['start_point']['x'] * x_scale)
        start_y = int(rect['start_point']['y'] * y_scale)
        end_x = int(rect['end_point']['x'] * x_scale)
        end_y = int(rect['end_point']['y'] * y_scale)

        resized_rectangles.append({
            "start_point": {"x": start_x, "y": start_y},
            "end_point": {"x": end_x, "y": end_y},
            "count": count
        })
        count += 1

    # 獲取當前時間並格式化為指定格式
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{current_time}.json"

    # 將轉換後的矩形數據保存到新的 JSON 文件
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(resized_rectangles, f, ensure_ascii=False, indent=4)

    print(f"縮放後的矩形數據已保存到 '{file_name}'。")

if __name__ == "__main__":
    resize_coordinates()
