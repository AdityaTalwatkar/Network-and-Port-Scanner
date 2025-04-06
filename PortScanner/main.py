import argparse
import nmap
import requests

def argument_parser():
    parser = argparse.ArgumentParser(description="TCP port scanner, accepts a hostname/IP address and list of ports to scan. Attempts to identify the service running on a port.")
    parser.add_argument("host", help="Host IP address")
    parser.add_argument("ports", help="Comma-separated port list, such as 25,80,8000")
    var_args = vars(parser.parse_args())
    return var_args

def nmap_scan(host_id, port_num):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id, port_num)
    state = nm_scan[host_id]['tcp'][int(port_num)]['state']
    result = "[*] {} tcp/{} {}".format(host_id, port_num, state)
    return result

if __name__ == "__main__":
    try:
        user_args = argument_parser()
        host = user_args["host"]
        r = requests.get("http://"+host)
        
        if r.status_code == 200:  
            ports = user_args["ports"].split(",")
            for port in ports:
                print(port)
                print(nmap_scan(host, port.strip()))
        else:
            print("Machine not reachable")

    except AttributeError:
        print("Error, please provide the command-line argument before running.")