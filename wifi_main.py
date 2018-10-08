import sys
import subprocess
from subprocess import check_output
import time

#results = subprocess.Popen('netsh wlan show interface', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
#out, err = results.communicate()
def wifi_list():
    results = subprocess.check_output(["netsh", "wlan", "show", "network"])
    results = results.decode("ascii") # needed in python 3
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4: ]
    ssids = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    print(ssids)

#wifi_list()


def wifi_connect():
    wifi_name = input('Input the Wifi SSID :   ')
    print (wifi_name)
    output = check_output('netsh wlan connect ' + wifi_name, shell=True)
    print (output)
    time.sleep(5)



def wifi_connected():
    output = check_output('netsh wlan show interface', shell=True)
    output = output.decode("ascii") # needed in python 3
    output = output.replace("\r","")
    ls = output.split("\n")
    #ls = ls[4: ]
    info = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            info.append(ls[x])
        x += 1
    state = ls[7]
    SSID = ls[8]
    print (state, sep='\n')
    print (SSID)
    if state == '    State                  : connected':
        print ("well done")
    else:
        print("not correct")
        
    

#wifi_connected()
    

