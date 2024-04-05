#!/usr/bin/python3

import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout for the connection attempt
s.settimeout(5)

# Get the target IP address from the user
host = input("Please enter the IP you want to scan: ")

# Get the port number to scan from the user
port = int(input("Please enter the port you want to scan: "))

# Function to scan the specified port
def portScanner(port):
    # Attempt to connect to the specified port
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

# Call the portScanner function with the provided port number
portScanner(port)
