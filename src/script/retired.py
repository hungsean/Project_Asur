import time
from function import script as script_function
from frame import start as start_frame
from script import usual


def main():
    monitor_info = start_frame.monitors[start_frame.monitor_index]

    if script_function.check_multiple(['retired']) == False:
        print("[INFO] check not retired @script/retired.main")
        return
    
    time.sleep(1)

    script_function.click_button(monitor_info, (637, 640), (813, 700))
    if script_function.check_multiple(['retired_info']) == False:
        print("[INFO] check not retired_info @script/retired.main")
        return
    script_function.click_button(monitor_info, (927, 615), (1102, 676))

    time.sleep(1)

    if script_function.check_multiple(['retired_info_warning'], 5, 1, 0.25) == True:
        script_function.click_button(monitor_info, (707, 472), (880, 532))
    elif script_function.check_multiple(['retired_info_warning_1'], 3, 1, 0.25) == True:
        script_function.click_button(monitor_info, (705, 515), (882, 578))

    time.sleep(1)

    if script_function.check_multiple(['get_items']) == False:
        print("[INFO] check not get_items @script/retired.main")
        return
    script_function.click_button(monitor_info, (100, 500), (1200, 650))

    time.sleep(1)

    if script_function.check_multiple(['retired_info_equipment']) == False:
        print("[INFO] check not retired_info_equipment @script/retired.main")
        return
    script_function.click_button(monitor_info, (869, 514), (1045, 575))

    time.sleep(1)

    if script_function.check_multiple(['get_material']) == False:
        print("[INFO] check not get_material @script/retired.main")
        return
    script_function.click_button(monitor_info, (718, 540), (895, 601))

    time.sleep(1)

    if script_function.check_multiple(['get_items']) == False:
        print("[INFO] check not get_items @script/retired.main")
        return
    script_function.click_button(monitor_info, (100, 500), (1200, 650))

    time.sleep(1)

    usual.back()
    return
