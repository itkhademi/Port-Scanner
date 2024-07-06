# Port-Scanner
The scan_ports function takes three input arguments: the device name, the starting port number, and the ending port number for the scan. Then it scans all the ports in that range in three steps,
In the first step, it creates a TCP socket using the socket function.
Then, using the gethostbyname function, the IP address of the target host is obtained.
At the end, it is connected to the desired IP and port using the connect function. If the connection is successful, it can be concluded that that particular port is open. Then, it closes the connection using the close function and repeats all these steps for the next port.
