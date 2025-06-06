import socket
import sys
from datetime import datetime as dt

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python scanner.py <ip>")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time Started: {dt.now()}")
print("-" * 50)

try:
    for port in range(50, 85):  # Scanning ports from 50 to 85
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((target, port))  # Try to connect to the port
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server")
    sys.exit()
