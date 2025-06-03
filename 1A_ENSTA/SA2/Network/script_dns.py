from scapy.all import *

response = sr1(IP(dst="8.8.8.8")/UDP()/DNS(rd=1, qd=DNSQR(qname="www.google.com")))

response.show()

if response and response.haslayer(DNS):
    print("@IP de google.com :", response[DNS].an.rdata)
