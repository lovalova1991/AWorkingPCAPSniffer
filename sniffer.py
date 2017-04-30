import os
from scapy.layers.inet import Raw, rdpcap

array = []
result = []
print("Analizer")
print("Starting TCPDUMP...\n")

os.system("timeout 10 tcpdump -s 0 \"port 3000\" -i lo -w captured.pcap")

pack = rdpcap('captured.pcap')
file = open("output/received.jpeg", "wb")

array = []
for packet in pack:
    #if this packet got a payload, then it'll be added to an array
    if packet.getlayer(Raw):
        print('Found Payload:\t')
        l = packet[Raw].load
        print(l)
        file.write(l)
file.close()
print("Writing file...\n")
for element in array:
    file.write(bytes(l))
file.close()
