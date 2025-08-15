from re import DEBUG, S
from monitorcontrol import get_monitors
import enum

DEBUG_MODE = False  # Set to True for detailed output


class PowerMode(enum.IntEnum):
    ON = 1
    STANDBY = 2
    SUSPEND = 3
    SW_OFF = 4
    HW_OFF = 5


def monitor_name(idx, monitor):
    return monitor.get_vcp_capabilities()['model'] if DEBUG_MODE else idx + 1


def set_all_monitors_to(target_power_mode):
    for idx, monitor in enumerate(get_monitors()):
        with monitor:
            curr_power_mode = monitor.get_power_mode()
            print(f"Monitor {monitor_name(idx, monitor)} is in state {curr_power_mode}")
            if curr_power_mode != target_power_mode:
                print(f"setting power mode {target_power_mode}.")
                monitor.set_power_mode(target_power_mode)
                print(f"Monitor {monitor_name(idx, monitor)} set to Power Mode {target_power_mode}.")
            else:
                print(
                    f"Monitor {monitor_name(idx, monitor)} is already in Power Mode {target_power_mode}.")


if __name__ == "__main__":
    result = False
    for idx, monitor in enumerate(get_monitors()):
        with monitor:
            if monitor.get_power_mode() == PowerMode.ON:
                result = True
                print(f"Monitor {monitor_name(idx, monitor)} is in mode {monitor.get_power_mode()}")
                break

    if result:
        print("Setting all monitors to power mode 4 (s-off)...")
        set_all_monitors_to(PowerMode.SW_OFF)
    else:
        print("All monitors in standby. Tuirning them on...")
        set_all_monitors_to(PowerMode.ON)
