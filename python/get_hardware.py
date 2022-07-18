# -- Using: psutil 5.9.1 --

import psutil

import platform

def get_cpu():
    cpu_core_count = psutil.cpu_count(logical=False)
    cpu_logical_core_count = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    cpu_current_freq = f"{cpu_freq.current:.2f}"
    
    return cpu_core_count, cpu_logical_core_count, cpu_freq, cpu_current_freq
    
def get_memory():
    virtual_memory = psutil.virtual_memory()
    
    virtual_memory_available = virtual_memory.available / 1000000000
    virtual_memory_tot = virtual_memory.total / 1000000000
    virtual_memory_percent = virtual_memory.percent
    
    return virtual_memory_available, virtual_memory_tot, f"{virtual_memory_percent}%"
    
def get_disks():
    
    partitions = psutil.disk_partitions()
    
    partitions_info = dict()
    
    partition_number = 0
    
    for partition in partitions:
        mountpoint = partition.mountpoint
        file_system = partition.fstype
        
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            total_size = usage.total / 1000000000
            used = usage.used / 1000000000
            free = usage.free / 1000000000
            percent_used = f"{str(usage.percent)}%"
            
        except PermissionError:
            usage = "PermissionError - Disk Usage not available"
            continue
        
        partitions_info.update({partition_number:{"mountpoint": mountpoint, "fs": file_system, "total_size": total_size, "used": used, "free": free, "percent_used":percent_used}})
            
        partition_number += 1
        
    return partitions_info

def get_network():
    ...
    
def get_all_users():
    return psutil.users()

def get_system_information():
    uname = platform.uname()    
    return uname.system, uname.node, uname.release, uname.version, uname.machine