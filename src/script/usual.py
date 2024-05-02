
from function import script as script_function
from frame import start as start_frame

def back():
    monitor_info = start_frame.monitors[start_frame.monitor_index]
    if script_function.check_multiple(['have_back']) == False:
        print("[INFO] check not have_back @script/usual.back")
        return
    script_function.click_button(monitor_info, (30, 29), (83, 78))
    return