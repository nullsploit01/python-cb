import platform
import time

with open("system_report.txt", "w") as file:
    file.write(f"System Report for {time.asctime()}\n")
    file.write(f"Platform: {platform.platform()}" + "\n")
    file.write(f"Machine: {platform.machine()}" + "\n")
    file.write(f"Processor: {platform.processor()}" + "\n")
    file.write(f"System: {platform.system()}" + "\n")
    file.write(f"Version: {platform.version()}" + "\n")
    file.write(f"Python Implementation: {platform.python_implementation()}" + "\n")
    file.write(f"Python Version: {platform.python_version_tuple()}" + "\n")
    
print("System report generated successfully!")