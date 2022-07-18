# -- Using: psutil 5.9.1 --

import psutil

def get_cpu():
    cpu_core_count = psutil.cpu_count(logical=False)
    cpu_logical_core_count = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    cpu_current_freq = f"{cpu_freq.current:.2f}"
    
    return cpu_core_count, cpu_logical_core_count, cpu_freq, cpu_current_freq
    
def get_memory():
    virtual_memory = int(str(psutil.virtual_memory())) / 1000000000 
    swap_memory = int(str(psutil.swap_memory())) / 1000000000 
    return virtual_memory, swap_memory
    
def get_disks():
    ...

def get_network():
    ...
    
def get_all_users():
    return psutil.users()

def get_other_info():
    return psutil.boot_time()