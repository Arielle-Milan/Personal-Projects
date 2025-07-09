# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 18:43:04 2025

@author: atcha
"""

from scapy.all import sniff

#callback function that runs on each captured packet
def packet_callback(packet):
    print(packet.summary())  # Print short description of packet

#start sniffing packets (requires admin/root privileges)
print("Sniffing packets...")
sniff(prn=packet_callback, count=10)  # Capture 10 packets then stop
