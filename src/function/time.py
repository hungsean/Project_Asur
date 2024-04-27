import time


def reduce_frequency(start_time, period):
    elapsed_time = time.time() - start_time  # 計算迴圈執行所花費的時間
    sleep_time = period - elapsed_time  # 計算需要等待的時間
    if sleep_time > 0:
        time.sleep(sleep_time)  # 等待一定時間，以保持固定的頻率執行