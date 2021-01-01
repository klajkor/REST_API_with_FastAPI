import socket
import os
import subprocess
from models.log_items import LogItemPublicIP


def get_last_line_of_log(log_file: str):
    try:
        with open(log_file, 'r') as logf:
            lines = logf.read().splitlines()
            last_line_of_log = lines[-1]
    except FileNotFoundError as e:
        print("FILE NOT FOUND")
        last_line_of_log = f'Error: {e.__str__()}'
        print(last_line_of_log)
    return last_line_of_log


def get_ip_from_log(log_file: str):
    log_item = LogItemPublicIP()
    log_item.date = "Dec 01"
    log_item.time = "01:02:03"
    log_item.ip_address = "12.34.56.78/32"
    last_line = get_last_line_of_log(log_file)
    last_line = last_line.replace("  ", " ")
    fields = last_line.split(" ")
    log_item.date = fields[0] + " " + fields[1]
    log_item.time = fields[2]
    if last_line.find("changed") > 0:
        log_item.ip_address = fields[11]
    else:
        log_item.ip_address = fields[7]
    return log_item


def get_server_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        server_ip = s.getsockname()
    except OSError as e:
        server_ip = '127.0.0.1'
    except SystemError as e:
        server_ip = '127.0.0.1'
    finally:
        s.close()
    return server_ip


def determine_docker_host_ip_address():
    cmd = "ip route show"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return str(output).split(' ')[2]


def get_hostname():
    print(os.environ)
    return os.environ["HOSTNAME"]
