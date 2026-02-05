import subprocess


class WaypaperdManager:
    def __init__(self, cycle_length: int):
        self.daemon_script = "waypaper/waypaperd.py"
        self.command = f"python {self.daemon_script}"
        self.cycle_length = cycle_length

    def check(self) -> bool:
        """Return True if daemon is running"""
        try:
            subprocess.check_output(["pgrep", "-f", self.command], encoding='utf-8')
            return True
        except subprocess.CalledProcessError:
            return False

    def launch(self) -> bool:
        """Return True if daemon is launched successfully"""
        command = f"{self.command} {self.cycle_length}".split(" ")
        print(f"{command=}")
        if not self.check():
            subprocess.Popen(command, start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        else:
            return False

    def kill(self) -> bool:
        """Return True if daemon is killed successfully"""
        if self.check():
            subprocess.run(["pkill", "-f", self.command])
            return True
        else:
            return False
