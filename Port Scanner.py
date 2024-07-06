import argparse
import socket

def scan_ports(host, start_port, end_port):
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get IP of remote host
    remote_ip = socket.gethostbyname(host)
    
    # Scan ports
    end_port += 1
    for port in range(start_port, end_port):
        try:
            sock.connect((remote_ip, port))
            print ('Port ' + str(port) + ' is open')
            sock.close()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            pass

if __name__ == '__main__':
   
    # setup commandline arguments
    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('--host', action="store", dest="host", default='localhost')
    parser.add_argument('--startport', action="store", dest="start_port", default=1, type=int)
    parser.add_argument('--endport', action="store", dest="end_port", default=100, type=int)
   
    # parse arguments
    given_args = parser.parse_args()
    host, start_port, end_port = given_args.host, given_args.start_port, given_args.end_port
    scan_ports(host, start_port, end_port)