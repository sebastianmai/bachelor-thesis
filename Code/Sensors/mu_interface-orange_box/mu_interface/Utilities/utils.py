import socket
from dataclasses import dataclass

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    
class TimeFormat():
    file = '%Y-%m-%d_%H:%M:%S'
    log = '%d.%m.%Y. %H:%M:%S'
    data = '%Y-%m-%d %H:%M:%S:%f'