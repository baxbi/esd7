
from scapy.all import*

arp_p = ARP(op = 1, psrc = "192.168.244.128", pdst = "192.168.244", hwsrc = "00:0c:29:90:b9:6f")


packet = IP(dst="10.94.71.15")
send(packet)
packet.show()

