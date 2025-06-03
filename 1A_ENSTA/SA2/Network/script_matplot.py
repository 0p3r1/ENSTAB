from scapy.all import *

ans, unans = srloop(
                IP(src="8.8.8.8", dst="8.8.4.4")/ICMP(), 
                inter=0.1,
                timeout=0.1,
                count=100,
                verbose=False
            )

print(ans)

ans.multiplot(lambda x, y: (y[IP].src, (y.time, y[IP].id)), plot_xy=True)