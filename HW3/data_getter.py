import psutil
import platform
from datetime import datetime
import cpuinfo
import socket
import uuid
import re

def get_size(bytes: int, suffix="B") -> str:
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def System_information() -> dict:
    """get system information
    Returns:
        dict: system information
    """
    system_information = {}
    main={}
    main['name']="="*40, "System Information", "="*40
    uname = platform.uname()
    main['system'] = f"System: {uname.system}"
    main['node_name'] = f"Node Name: {uname.node}"
    main['release'] = f"Release: {uname.release}"
    main['version'] = f"Version: {uname.version}"
    main['machine'] = f"Machine: {uname.machine}"
    main['processor'] = f"Processor: {cpuinfo.get_cpu_info()['brand_raw']}"
    main['ip_address'] = f"Ip-Address: {socket.gethostbyname(socket.gethostname())}"
    main['mac_address'] = f"Mac-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}"
    
    system_information['main']=main
    # Boot Time
    main={}
    main['name']="="*40, "Boot Time", "="*40
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    main['boot_time'] = f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
    system_information['boot_time']=main
    main={}
    main['name']="="*40, "CPU Info", "="*40
    # number of cores
    main['physical_cores'] = f"Physical cores: {psutil.cpu_count(logical=False)}"
    main['total_cores'] = f"Total cores: {psutil.cpu_count(logical=True)}"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    main['max_frequency'] = f"Max Frequency: {cpufreq.max:.2f}Mhz"
    main['min_frequency'] = f"Min Frequency: {cpufreq.min:.2f}Mhz"
    main['current_frequency'] = f"Current Frequency: {cpufreq.current:.2f}Mhz"
    # CPU usage
    main['cpu_usage_per_core'] = "CPU Usage Per Core:"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        main['cpu_usage_per_core'] += f"Core {i}: {percentage}%"
    main['total_cpu_usage'] = f"Total CPU Usage: {psutil.cpu_percent()}%"
    system_information['cpu_info']=main
    

    # Memory Information
    main={}
    main['name']="="*40, "Memory Information", "="*40
    # get the memory details
    svmem = psutil.virtual_memory()
    main['total'] = f"Total: {get_size(svmem.total)}"
    main['available'] = f"Available: {get_size(svmem.available)}"
    main['used'] = f"Used: {get_size(svmem.used)}"
    main['percentage'] = f"Percentage: {svmem.percent}%"
    system_information['memory_info']=main
    # Swap Memory
    main={}
    main['name']="="*40, "Swap Memory", "="*40
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    main['total'] = f"Total: {get_size(swap.total)}"
    main['free'] = f"Free: {get_size(swap.free)}"
    main['used'] = f"Used: {get_size(swap.used)}"
    main['percentage'] = f"Percentage: {swap.percent}%"
    

  
       
    system_information['swap_memory']=main

    ## Network information

    ##get IO statistics since boot
    main={}
    net_io = psutil.net_io_counters()
    main['name']="="*40, "Network Information", "="*40
    main['bytes_sent'] = f"Total Bytes Sent: {get_size(net_io.bytes_sent)}"
    main['bytes_recv'] = f"Total Bytes Received: {get_size(net_io.bytes_recv)}"
    system_information['network_info']=main
    # Disk Information
    return system_information