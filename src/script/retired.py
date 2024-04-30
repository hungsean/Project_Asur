
from function import script as script_function
from frame import start as start_frame


def main():
    monitor_info = start_frame.monitors[start_frame.monitor_index]
    if script_function.check_multiple(['retired'], 2, 0.5) == False:
        print("[INFO] check not retired @script/retired.main")
        return
    script_function.click_button(monitor_info, (637, 640), (813, 700))

    