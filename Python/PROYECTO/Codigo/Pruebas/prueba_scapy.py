#!/usr/bin/env python
from multiprocessing import Process
try:
    from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11ProbeResp, Dot11Elt
    from scapy.all import *
except Exception, e:
    print 'Failed to import scapy:',e
    exit(1)
    

interface = "wlp1s0mon"
ap_list = []
subtypes = (0, 2, 4, 8)#(0, 2, 4, 8) #subtype 8 == Beacon frame

def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        try:       #type 4 == ProbRequest
            if pkt.type == 0  and pkt.subtype in subtypes:
                if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
                    try:
                        extra = pkt.notdecoded
                        rssi = -(256-ord(extra[-4:-3]))
                    except:
                        rssi = -100
                    try:
                        channel = int(ord(pkt[Dot11Elt:3].info))
                    except:
                        channel = 0
                    if pkt.addr2 not in ap_list:
                        ap_list.append(pkt.addr2)
                        print '\033[94m MAC:\033[0m %s  \033[94m SSID:\033[0m %17.13s  \033[94mRSSI:\033[0m %d dBm  \033[94m Channel:\033[0m %d' \
                              %(pkt.addr2, pkt.info, int(rssi), int(channel))
        except AttributeError:
            pass


def User_ESSID(pkt):
    if pkt.haslayer(Dot11):
        try:
            if pkt.type == 0 and pkt.subtype in subtypes:
                if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
                    print pkt.summary()
                    print pkt.show()
                    print pkt.show2()
        except AttributeError:
            pass

def Channel_Hopper():
    while True:
        try:
            chan = random.randrange(1, 13)  # 13 canales legales en europa
            os.system('iw dev %s set channel %d' % (interface, chan))
            print '\033[91m Channel Changed to: %d \033[0m' %chan
            time.sleep(1)
        except:
            print '\033[91m [ERROR]---Error changing channel  \033[0m'
            break



if __name__ == "__main__":
    p = Process(target=Channel_Hopper)
    p.start()


    sniff(iface=interface, prn=User_ESSID)


