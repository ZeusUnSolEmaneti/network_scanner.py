import scapy.all as sa
import optparse
import os

os.system("clear")

#1)Arp Request
#2)Broadcast
#3)Response


print("""
█▀▀▄ █▀▀ ▀▀█▀▀ █░░░█ █▀▀█ █▀▀█ █░█     █▀▀ █▀▀ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█
█░░█ █▀▀ ░░█░░ █▄█▄█ █░░█ █▄▄▀ █▀▄     ▀▀█ █░░ █▄▄█ █░░█ █░░█ █▀▀ █▄▄▀
▀░░▀ ▀▀▀ ░░▀░░ ░▀░▀░ ▀▀▀▀ ▀░▀▀ ▀░▀     ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀ ▀░▀▀
""")


parse_object=optparse.OptionParser()
parse_object.add_option("-i","--ip",dest="arp_request",help="Arp Request")
(user_inputs,arguments)=parse_object.parse_args()
arp_request=sa.ARP(pdst=user_inputs.arp_request)#arp isteği gönderir
broadcast_packet=sa.Ether(dst="ff:ff:ff:ff:ff:ff") #broadcast yayını yapar ve ip macleri alır
combined_packet = broadcast_packet/arp_request #iki paketi birleştirmeye yarar
(answered_list,unanswered_list)=result= sa.srp(combined_packet,timeout=1)
answered_list.summary()
#print(result)
#sa.ls(sa.Ether())
