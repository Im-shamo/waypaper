import os
import subprocess
def symlink_wallpaper(image_path: str, symlink_path: str):
    command = ["ln", "-sf"]
    command.append(image_path)
    command.append(symlink_path)
    subprocess.Popen(command)

if __name__ == "__main__":
    image_path = input()
    symlink_wallpaper(image_path)