# -- Using: psutil 5.9.1 --

import psutil

def get_process():
    proc_dict = dict()
    n = 0
    
    for proc in psutil.process_iter(['pid', 'name']):
        proc_dict.update({n: proc.info})
        n += 1
        
    return proc_dict
    
    
    
