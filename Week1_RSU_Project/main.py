#The script essentially provides a quick snapshot of your system's resource usage.
import psutil

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
print("The datas below are providing a quick snapshot of your system's resource usage.")
print(f"CPU: {cpu}%")
print(f"RAM: {ram}%")
print(f"Disk: {disk}%")