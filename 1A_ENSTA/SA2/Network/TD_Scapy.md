# TD sur la bibliothèque Scapy

---
**SEDDOUGUI Shems-Eddine**
> FIPASE 27  
> 2025-06-03
---

## Installation de la bibliothèque Scapy

Étant sur `MacOS`, je suis la méthode d'installation `Linux`.

### Clonage du dépôt Scapy

Je télécharge `scapy` depuis le dépôt GitHub officiel :

```sh
➜  r00tme git clone --depth 1 https://github.com/secdev/scapy
Clonage dans 'scapy'...
remote: Enumerating objects: 906, done.
remote: Counting objects: 100% (906/906), done.
remote: Compressing objects: 100% (860/860), done.
remote: Total 906 (delta 60), reused 454 (delta 33), pack-reused 0 (from 0)
Réception d'objets: 100% (906/906), 6.92 Mio | 1.43 Mio/s, fait.
Résolution des deltas: 100% (60/60), fait.
```

Je me déplace ensuite dans le dossier `scapy` et je lance `scapy` via le script fourni :

```sh
➜  r00tme cd scapy
➜  scapy git:(master) ./run_scapy
INFO: Can't import PyX. Won't be able to use psdump() or pdfdump().
WARNING: No alternative Python interpreters found ! Using standard Python shell instead.
INFO: Using the default Python shell: History is disabled.

                     aSPY//YASa
             apyyyyCY//////////YCa       |
            sY//////YSpcs  scpCY//Pp     | Welcome to Scapy
 ayp ayyyyyyySCP//Pp           syY//C    | Version 2025.06.03
 AYAsAYYYYYYYY///Ps              cY//S   |
         pCCCCY//p          cSSps y//Y   | https://github.com/secdev/scapy
         SPPPP///a          pP///AC//Y   |
              A//A            cyP////C   | Have fun!
              p///Ac            sC///a   |
              P////YCpc           A//A   | To craft a packet, you have to be a
       scccccp///pSP///p          p//Y   | packet, and learn how to swim in
      sY/////////y  caa           S//P   | the wires and in the waves.
       cayCyayP//Ya              pY/Ya   |        -- Jean-Claude Van Damme
        sY/PsY////YCc          aC//Yp    |
         sc  sccaCY//PCypaapyCP//YSs
                  spCPY//////YPSps
                       ccaacs

>>>
```

### Installation des dépendances supplémentaires

On remarque un message d'avertissement qui indique que la bibliothèque `PyX` n'est pas installée. Elle est requise pour certaines fonctionnalités graphiques de `scapy`, comme `psdump()` ou `pdfdump()`. Je l'installe donc via `pip` :

```sh
➜  scapy git:(master) pip install pyx
Collecting pyx
  Downloading PyX-0.16.tar.gz (626 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 626.7/626.7 kB 671.2 kB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: pyx
  Building wheel for pyx (pyproject.toml) ... done
  Created wheel for pyx: filename=pyx-0.16-py3-none-any.whl size=437451 sha256=f3cf5e1d581d1d0f466fb51c1ab86c52680931ccc3a5c3c62ed5b17e6bb57769
  Stored in directory: /Users/serguei/Library/Caches/pip/wheels/d0/9e/c4/1b4f29ec2263ef23fb51b5eed809ff16a93f17a8bf2dc65846
Successfully built pyx
Installing collected packages: pyx
Successfully installed pyx-0.16

[notice] A new release of pip is available: 24.3.1 -> 25.1.1
[notice] To update, run: pip install --upgrade pip
```

On relance `scapy` pour être sûr qu'aucune dépendance n'est manquante.

```sh
➜  scapy git:(master) ./run_scapy
INFO: PyX dependencies are not installed ! Please install TexLive or MikTeX.
WARNING: No alternative Python interpreters found ! Using standard Python shell instead.
INFO: Using the default Python shell: History is disabled.

                     aSPY//YASa
             apyyyyCY//////////YCa       |
            sY//////YSpcs  scpCY//Pp     | Welcome to Scapy
 ayp ayyyyyyySCP//Pp           syY//C    | Version 2025.06.03
 AYAsAYYYYYYYY///Ps              cY//S   |
         pCCCCY//p          cSSps y//Y   | https://github.com/secdev/scapy
         SPPPP///a          pP///AC//Y   |
              A//A            cyP////C   | Have fun!
              p///Ac            sC///a   |
              P////YCpc           A//A   | Craft me if you can.
       scccccp///pSP///p          p//Y   |                   -- IPv6 layer
      sY/////////y  caa           S//P   |
       cayCyayP//Ya              pY/Ya
        sY/PsY////YCc          aC//Yp
         sc  sccaCY//PCypaapyCP//YSs
                  spCPY//////YPSps
                       ccaacs

>>>
```

On observe que `PyX` est bien installé, mais que `scapy` signale toujours un avertissement :

`INFO: PyX dependencies are not installed ! Please install TexLive or MikTeX.`

Ces dépendances sont nécessaires uniquement pour les fonctionnalités de génération de graphiques mais on procède tout de même à l'installation de `TexLive` :

```sh
➜  scapy git:(master) brew install texlive
```

Après de longues minutes d'attente, `TexLive` est enfin installé. On vérifie que tout est bon en relançant `scapy` :

```sh
➜  scapy git:(master) ./run_scapy
WARNING: No alternative Python interpreters found ! Using standard Python shell instead.
INFO: Using the default Python shell: History is disabled.

                     aSPY//YASa
             apyyyyCY//////////YCa       |
            sY//////YSpcs  scpCY//Pp     | Welcome to Scapy
 ayp ayyyyyyySCP//Pp           syY//C    | Version 2025.06.03
 AYAsAYYYYYYYY///Ps              cY//S   |
         pCCCCY//p          cSSps y//Y   | https://github.com/secdev/scapy
         SPPPP///a          pP///AC//Y   |
              A//A            cyP////C   | Have fun!
              p///Ac            sC///a   |
              P////YCpc           A//A   | To craft a packet, you have to be a
       scccccp///pSP///p          p//Y   | packet, and learn how to swim in
      sY/////////y  caa           S//P   | the wires and in the waves.
       cayCyayP//Ya              pY/Ya   |        -- Jean-Claude Van Damme
        sY/PsY////YCc          aC//Yp    |
         sc  sccaCY//PCypaapyCP//YSs
                  spCPY//////YPSps
                       ccaacs

>>>
```

## Premiers pas

### Commandes de base

Pour commencer, on crée un paquet IP avec un segment TCP, puis on l'encapsule dans une trame Ethernet :

```py
>>> packet = IP()/TCP()
>>> Ether()/packet
<Ether  type=IPv4 |<IP  frag=0 proto=tcp |<TCP  |>>>
```

On affiche tout le contenu du paquet :

```py
>>> packet.show()
###[ IP ]###
  version   = 4
  ihl       = None
  tos       = 0x0
  len       = None
  id        = 1
  flags     =
  frag      = 0
  ttl       = 64
  proto     = tcp
  chksum    = None
  src       = 127.0.0.1
  dst       = 127.0.0.1
  \options   \
###[ TCP ]###
     sport     = ftp_data
     dport     = http
     seq       = 0
     ack       = 0
     dataofs   = None
     reserved  = 0
     flags     = S
     window    = 8192
     chksum    = None
     urgptr    = 0
     options   = []
```

On affiche le contenu de la couche IP :

```py
>>> ls(IP)
version    : BitField  (4 bits)                  = ('4')
ihl        : BitField  (4 bits)                  = ('None')
tos        : XByteField                          = ('0')
len        : ShortField                          = ('None')
id         : ShortField                          = ('1')
flags      : FlagsField                          = ('<Flag 0 ()>')
frag       : BitField  (13 bits)                 = ('0')
ttl        : ByteField                           = ('64')
proto      : ByteEnumField                       = ('0')
chksum     : XShortField                         = ('None')
src        : SourceIPField                       = ('None')
dst        : DestIPField                         = ('None')
options    : PacketListField                     = ('[]')
```

On affiche le contenu de la couche TCP :

```py
>>> ls(TCP)
sport      : ShortEnumField                      = ('20')
dport      : ShortEnumField                      = ('80')
seq        : IntField                            = ('0')
ack        : IntField                            = ('0')
dataofs    : BitField  (4 bits)                  = ('None')
reserved   : BitField  (3 bits)                  = ('0')
flags      : FlagsField                          = ('<Flag 2 (S)>')
window     : ShortField                          = ('8192')
chksum     : XShortField                         = ('None')
urgptr     : ShortField                          = ('0')
options    : TCPOptionsField                     = ("b''")
```

On affiche un résumé d'informations de notre paquet :

```py
>>> packet.summary()
'IP / TCP 127.0.0.1:ftp_data > 127.0.0.1:http S'
```

Sur le même paquet, on peut afficher l'@IP source :

```py
>>> packet.src
'127.0.0.1'
>>> packet[IP].src
'127.0.0.1'
```

Mais on ne peut pas afficher d'@MAC car le paquet `packet` ne contient pas de couche Ethernet, donc il n’a pas d’adresse MAC.

Si on avait une couche Ethernet, ce serait :

```py
>>> packet[Ether].dst
```

On affiche le type, le port source et destination de la couche TCP dans `scapy` :

```py
>>> TCP().name
'TCP'
>>> TCP().sport
20
>>> TCP().dport
80
```

On peut faire des paquets de manière plus implicite. Par exemple, si on peut faire varier le TTL pour imiter un traceroute :

```py
>>> [p for p in IP(ttl=(1,5))/ICMP()]
[<IP  frag=0 ttl=1 proto=icmp |<ICMP  |>>, <IP  frag=0 ttl=2 proto=icmp |<ICMP  |>>, <IP  frag=0 ttl=3 proto=icmp |<ICMP  |>>, <IP  frag=0 ttl=4 proto=icmp |<ICMP  |>>, <IP  frag=0 ttl=5 proto=icmp |<ICMP  |>>]
```

### Envoi et réception de paquets

On installe `scapy` dans notre environnement :

```sh
➜  scapy git:(master) pip install .
Processing /Users/serguei/r00tme/scapy
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: scapy
  Building wheel for scapy (pyproject.toml) ... done
  Created wheel for scapy: filename=scapy-2025.6.3-py3-none-any.whl size=2459984 sha256=98c9508c6bcae2d4556fe8487b59a29b731ee7de8397b61dcf6ff1dd2e9a5042
  Stored in directory: /private/var/folders/xk/4l7tsx8x6q3cd7cx5sfn_7g40000gn/T/pip-ephem-wheel-cache-ys6swr77/wheels/62/ee/1e/a8bc63ff6489556baaa1c949a3512f201924cb1f38a1cfa18e
Successfully built scapy
Installing collected packages: scapy
Successfully installed scapy-2025.6.3

[notice] A new release of pip is available: 24.3.1 -> 25.1.1
[notice] To update, run: pip install --upgrade pip
```

Voici un code qui permet de récupérer l’@IP de `google.com` :

```py
# script.py

from scapy.all import *

response = sr1(IP(dst="8.8.8.8")/UDP()/DNS(rd=1, qd=DNSQR(qname="www.google.com")))

response.show()

if response and response.haslayer(DNS):
    print("@IP de google.com :", response[DNS].an.rdata)
```

```sh
➜  Network git:(main) ✗ python3 script.py 
Begin emission
..
Finished sending 1 packets
..*
Received 5 packets, got 1 answers, remaining 0 packets
###[ IP ]###
  version   = 4
  ihl       = 5
  tos       = 0x0
  len       = 76
  id        = 17566
  flags     = 
  frag      = 0
  ttl       = 118
  proto     = udp
  chksum    = 0x39dd
  src       = 8.8.8.8
  dst       = 172.20.10.2
  \options   \
###[ UDP ]###
     sport     = domain
     dport     = domain
     len       = 56
     chksum    = 0xbb20
###[ DNS ]###
        id        = 0
        qr        = 1
        opcode    = QUERY
        aa        = 0
        tc        = 0
        rd        = 1
        ra        = 1
        z         = 0
        ad        = 0
        cd        = 0
        rcode     = ok
        qdcount   = 1
        ancount   = 1
        nscount   = 0
        arcount   = 0
        \qd        \
         |###[ DNS Question Record ]###
         |  qname     = b'www.google.com.'
         |  qtype     = A
         |  unicastresponse= 0
         |  qclass    = IN
        \an        \
         |###[ DNS Resource Record ]###
         |  rrname    = b'www.google.com.'
         |  type      = A
         |  cacheflush= 0
         |  rclass    = IN
         |  ttl       = 18
         |  rdlen     = None
         |  rdata     = 216.58.214.68
        \ns        \
        \ar        \

@IP de google.com : 216.58.214.68
```

On observe qu'un seul paquet a été envoyé pour effectuer la requête DNS.

### Interaction avec des fichiers PCAP

Affichons le contenu du premier paquet `nb6-telephone.pcap` dans les ateliers Wireshark du dépôt Gitlab :

```py
# script_pcap.py

from scapy.all import rdpcap

pcap_p = rdpcap("wireshark/nb6-telephone.pcap")

print(pcap_p[0].summary())
pcap_p[0].show()
```

```sh
➜  Network git:(main) ✗ python3 script_pcap.py
Ether / PPPoE / PPP / IP / UDP / L2TP / PPP / LCP Echo-Request
###[ Ethernet ]###
  dst       = e0:a1:d7:18:c2:73
  src       = 00:17:33:61:00:00
  type      = PPPOE
###[ PPP over Ethernet ]###
     version   = 1
     type      = 1
     code      = Session
     sessionid = 0x4e3f
     len       = 54
###[ PPP Link Layer ]###
        proto     = Internet Protocol version 4
###[ IP ]###
           version   = 4
           ihl       = 5
           tos       = 0xc0
           len       = 52
           id        = 51713
           flags     = 
           frag      = 0
           ttl       = 250
           proto     = udp
           chksum    = 0x35bd
           src       = 109.6.1.72
           dst       = 95.136.242.99
           \options   \
###[ UDP ]###
              sport     = l2f
              dport     = l2f
              len       = 32
              chksum    = 0x0
###[ L2TP ]###
                 hdr       = priority+offset
                 version   = L2TPv2
                 tunnel_id = 34203
                 session_id= 48303
                 offset    = 0
###[ PPP Link Layer ]###
                    proto     = Link Control Protocol
###[ PPP Link Control Protocol ]###
                       code      = Echo-Request
                       id        = 0x5a
                       len       = 12
                       magic_number= 3178488472
                       data      = b'\x93^I\xbc'
```

### Affichage de résultats avec Matplotlib

On envoie 100 paquets ICMP de 8.8.8.8 vers 8.8.4.4. On utilise la fonction srloop(), puis on affiche les ID des paquets IP :

```py
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
```

```sh
➜  Network git:(main) ✗ python3 script_matplot.py
<Results: TCP:0 UDP:0 ICMP:0 Other:0>
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/scapy/plist.py:387: UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
  plt.legend(loc="center right", bbox_to_anchor=(1.5, 0.5))
```

![](@attachment/Clipboard_2025-06-03-09-52-22.png)

On observe que `scapy` n'a reçu aucune réponse aux 100 paquets envoyés... sûrement dû à une protection anti-spoofing.

### Capturer des paquets sur le réseau

```py
# script_sniff.py

from scapy.all import *

pkts = sniff(filter='icmp', count=2, iface='en0')

pkts.summary()
pkts[0].show()
```