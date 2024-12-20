import platform
import os

def es_powershell():
    return 'PSModulePath' in os.environ

def system_type():
    so = platform.system()
    if so == "Windows":
        if es_powershell():
            return "PowerShell en windows"
        else:
            return "CMD en windows"
    elif so == "Linux":
        return "linux"
    elif so == "Darwin":
        return "MacOs"
    else:
        return ""
