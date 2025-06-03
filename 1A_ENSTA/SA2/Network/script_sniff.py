from scapy.all import *

pkts = sniff(filter='icmp', count=2, iface='en0')

pkts.summary()
pkts[0].show()
