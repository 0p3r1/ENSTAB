from scapy.all import rdpcap

pcap_p = rdpcap("wireshark/nb6-telephone.pcap")

print(pcap_p[0].summary())
pcap_p[0].show()
