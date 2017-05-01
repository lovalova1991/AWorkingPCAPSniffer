import os
from scapy.layers.inet import Raw, rdpcap
from utils import output

def sniffer(out_lck, timeout, port, interface):

    output(out_lck, "Analizer")
    output(out_lck, "Starting TCPDUMP...\n")

    os.system("timeout " + str(timeout) + " tcpdump -s 0 \"port " + str(port) + "\" -i " + interface + " -w captured.pcap")

    pack = rdpcap('captured.pcap')
    file = open("output/sniffed.jpeg", "wb")

    if len(pack) > 0:
        for packet in pack:
            #if this packet got a payload, then it'll be printed in the sniffed file
            if packet.getlayer(Raw):
                output(out_lck, 'Found Payload:\t')
                l = packet[Raw].load
                output(out_lck, l)
                file.write(l)
        file.close()

    else:
        print("Nothing captured..\nExiting....")
        exit(5)
