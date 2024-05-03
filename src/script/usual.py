
from function import script as script_function
from frame import start as start_frame

def back():
    monitor_info = start_frame.monitors[start_frame.monitor_index]
    if script_function.check_multiple(['have_back']) == False:
        print("[INFO] check not have_back @script/usual.back")
        return
    script_function.click_button(monitor_info, (30, 29), (83, 78))
    return

def total_rewards():
    monitor_info = start_frame.monitors[start_frame.monitor_index]
    if script_function.check_multiple(['total_rewards']) == False:
        print("[INFO] check not total_rewards @script/usual.total_rewards")
        return
    script_function.click_button(monitor_info, (771, 596), (921, 649))
    return

def total_rewards_stop():
    monitor_info = start_frame.monitors[start_frame.monitor_index]
    if script_function.check_multiple(['total_rewards_stop']) == False:
        print("[INFO] check not total_rewards_stop @script/usual.total_rewards_stop")
        return
    script_function.click_button(monitor_info, (771, 596), (921, 649))
    return

def total_rewards_stop_1():
    monitor_info = start_frame.monitors[start_frame.monitor_index]
    if script_function.check_multiple(['total_rewards_stop_1']) == False:
        print("[INFO] check not total_rewards_stop_1 @script/usual.total_rewards_stop_1")
        return
    script_function.click_button(monitor_info, (842, 597), (991, 649))
    return

def start_sorties():
    monitor_info = start_frame.monitors[start_frame.monitor_index]
    if script_function.check_multiple(['start_sorties']) == False:
        print("[INFO] check not start_sorties @script/usual.start_sorties")
        return
    script_function.click_button(monitor_info, (773, 442), (948, 503))
    return