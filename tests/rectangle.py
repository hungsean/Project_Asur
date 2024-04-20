import json
import datetime

def main():
    rectangles = []
    print("請輸入矩形的起始座標(x, y)和長寬，或輸入'stop'終止：")
    count = 0
    while True:
        # 接收用戶輸入，如果輸入為'stop'則終止
        user_input = input()
        if user_input.lower() == 'stop':
            break
        
        # 解析輸入，預期輸入格式為 "x y width height"
        try:
            x, y, width, height = map(int, user_input.split())
            # 計算終點座標
            x2 = x + width
            y2 = y + height
            
            # 保存矩形信息
            rectangle = {
                "start_point": {"x": x, "y": y},
                "end_point": {"x": x2, "y": y2},
                "count": count
            }
            count += 1
            rectangles.append(rectangle)
        except ValueError:
            print("輸入格式錯誤，請重新輸入。格式應為：x y width height")

    # 獲取當前時間並格式化為指定格式
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"garbage\\{current_time}.json"

    # 將矩形數據保存到 JSON 文件
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(rectangles, f, ensure_ascii=False, indent=4)

    print(f"矩形數據已保存到 '{file_name}'。")

if __name__ == "__main__":
    main()
