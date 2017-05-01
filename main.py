import threading
from utils import *
from client import *
from server import *
from poisoner import *
from sniffer import *

if __name__ == "__main__":

    out_lck = threading.Lock()

    #Change those parameters
    host = "127.0.0.1"
    port = 3000
    interface = "lo"
    extension = "jpg"

    while True:
        # Main Menu
        logo()
        main_menu = loop_menu(out_lck, "\n\nSelect one of the following actions ('e' to exit): ", ["Send file",
                                                                                               "Receive file",
                                                                                               "MiTm",
                                                                                               "Sniffer"])
        if main_menu == 1:
            option = loop_menu(out_lck, "Select an option: ", ["TCP",
                                                               "UDP"])
            if option == 1:
                TCPclient(out_lck, host, port)
            elif option == 2:
                UDPclient(out_lck, host, port)


        elif main_menu == 2:
            option = loop_menu(out_lck, "Select an option: ", ["TCP",
                                                               "UDP"])
            if option == 1:
                TCPserver(out_lck, host, port, extension)
            elif option == 2:
                UDPserver(out_lck, host, port, extension)


        elif main_menu == 3:
            option = loop_menu(out_lck, "Select an option: ", ["Arp Poisoner",
                                                               "MAC Flooding"])
            if option == 1:
                arpoisoner(out_lck, interface)
            elif option == 2:
                macflooder(out_lck, interface)


        elif main_menu == 4:
            time = loop_input(out_lck, "Please insert a timeout:")
            sniffer(out_lck, time, port, interface)


        else:
            output(out_lck, "Please insert a valid option...\n")
