def filter_dicts(names, dict_list):
    # 將 names 轉換為集合以提高查找效率
    name_set = set(names)
    # 初始化輸出陣列
    output_dicts = []
    # 遍歷 dict_list，檢查每個字典的 "name" 是否存在於 name_set 中
    for item in dict_list:
        if item['name'] in name_set:
            output_dicts.append(item)
    if len(output_dicts) != len(names):
        print("[ERROR] have name not exist @filter_dicts")
        return None
    return output_dicts


# 範例字典列表
dict_list = [
    {"name": "Alice", "sample": 1, "coordsArray": [0, 1, 2]},
    {"name": "Bob", "sample": 2, "coordsArray": [1, 2, 3]},
    {"name": "Diana", "sample": 3, "coordsArray": [2, 3, 4]}
]

# 範例名字陣列
names = ['Alice', 'Bob']

# 調用函數
filtered_names = filter_dicts(names, dict_list)
print(filtered_names)  # 輸出: ['Alice', 'Bob']
