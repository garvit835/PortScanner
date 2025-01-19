import pyfiglet
import os
import socket
from termcolor import colored
from datetime import datetime

#To get the terminal width
terminal_width = os.get_terminal_size().columns

#Displaying the ASCII art of the program along with version
version = pyfiglet.figlet_format("v1 . 0 . 0", font="small", width=terminal_width, justify="left")
ascii_art = pyfiglet.figlet_format("Port Scanner", font="starwars", width=terminal_width, justify="center")
centered_art = ascii_art.center(terminal_width)

print(colored("-" * terminal_width, "red"))
print(colored(centered_art, "yellow"))
print(colored(version, "green"))
print(colored("-" * terminal_width, "blue"))

#Taking the input from the user for the target ip or website
target = input(colored("Enter the web address or ip address you want to scan: ", "magenta"))

#Taking the input from the user for the port range
port_range_input = input(colored("Range of ports: (e.g. 0-1026 or 80 ) ", "magenta"))

#Checking if the user has entered a range of ports or a single port
if '-' in port_range_input:
    #Splitting the port range into start and end ports
    start_port, end_port = port_range_input.split('-')
    try:
        #Converting the port numbers to integers
        start_port = int(start_port)
        end_port = int(end_port)
        #Entering the port numbers in the range into a list
        ports = range(start_port, end_port + 1)
        #Checking if the port numbers are valid
    except ValueError:
        print(colored("Invalid port range. Please enter valid integer values.", "red"))
        ports = []
        #If the user has entered a single port number
else:
    try:
        port_num = int(port_range_input)
        ports = [port_num]
    except ValueError:
        print(colored("Invalid port number. Please enter a valid integer.", "red"))
        ports = []

#Asking the user if they want to save the results to a log file
save_choice = input(colored("Do you want to save the results to a file? (yes/no): ", "magenta"))

#Initializing the scan results list
scan_results = []

#Scanning the target for open ports
print(f"Scanning started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
print(colored(f"Scanning {target} for open ports...\n", "blue"))

for port in ports:
    try:
        #Creating a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Setting the timeout for the connection
        socket.setdefaulttimeout(1)
        #Connecting to the target
        result = s.connect_ex((target, port))
        #Checking the result of the connection
        if result == 0:
            scan_results.append(colored(f"Port {port} is open", "green"))
        elif result == 111:
            scan_results.append(colored(f"Port {port} is closed", "red"))
        else:
            scan_results.append(colored(f"Port {port} is filtered", "yellow"))
        s.close()
    except KeyboardInterrupt:
        exit()
    except socket.gaierror:
        exit()
    except socket.error:
        scan_results.append(colored(f"Server {target} is unreachable (server is down)", "red"))

#Displaying the scan results
for result in scan_results:
    print(result)

#Saving the scan results to a log file
if save_choice in ["yes", "y"]:
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file_name = f"scan_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(log_file_name, "w") as log_file:
        log_file.write(f"Scan Results for {target} at {current_time}:\n")
        log_file.write("\n".join(scan_results) + "\n")
    print(colored(f"Scan results saved to '{log_file_name}' at {current_time}.", "blue"))
else:
    print(colored(f"Scan results were not saved. Time: {current_time}", "yellow"))