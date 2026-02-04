import os.path
import subprocess

daemon_script = "waypaper/waypaperd.py"
search_str = f"python {daemon_script}"
cycle_length = 60

def check_daemon() -> bool:
    """Return True if daemon is running"""
    try:
        subprocess.check_output(["pgrep", "-f", search_str], encoding='utf-8')
        return True
    except subprocess.CalledProcessError:
        return False


def launch_daemon() -> bool:
    """Return True if daemon is launched successfully"""
    if not check_daemon():
        subprocess.Popen(['python', daemon_script, str(cycle_length)], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    else:
        return False


def kill_daemon() -> bool:
    """Return True if daemon is killed successfully"""
    if check_daemon():
        subprocess.run(["pkill", "-f", search_str])
        return True
    else:
        return False


def get_cycle_length() -> int | None:
    try:
        input_massage = "Enter number of second per cycle\n> "
        user_input = int(input(input_massage))
        return user_input
    except ValueError:
        return None
