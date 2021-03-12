#!/usr/bin/python3
# Dbrute: Sub Directory Brute-Forcing Tool
# Author - Himanshu Shukla (etc5had0w)
# Version -1.0
# Disclaimer - Use this tool on your own risk. Creator of this tool will not be held responsible for any harm caused by usage of this tool.
# Make sure all dependencies are installed before running this program.
# Report any errors or issues found to the github page directly.
# Note - Copying, Modifying or Reproducing this code is not allowed without prior permission of the owner of this program.

import requests 
import argparse
import multiprocessing as mp
import time

RESET = '\033[m' 
BackgroundBlack = "\033[40m"
Black        = "\033[30m"
Red          = "\033[31m"
Green        = "\033[32m"
Yellow       = "\033[33m"
Blue         = "\033[34m"
Magenta      = "\033[35m"
Cyan         = "\033[36m"
LightGray    = "\033[37m"
DarkGray     = "\033[90m"
LightRed     = "\033[91m"
LightGreen   = "\033[92m"
LightYellow  = "\033[93m"
LightBlue    = "\033[94m"
LightMagenta = "\033[95m"
LightCyan    = "\033[96m"
White        = "\033[97m"
Blink      = "\033[5m"
BOLD = '\033[1m'


def logo():
    print (BOLD+Yellow+"\n     _ _                _       ",RESET)
    print (BOLD+Yellow+"  __| | |__  _ __ _   _| |_ ___ ",RESET)
    print (BOLD+Yellow+" / _` | '_ \| '__| | | | __/ _ \\",RESET)
    print (BOLD+Yellow+"| (_| | |_) | |  | |_| | ||  __/",RESET)
    print (BOLD+Yellow+" \__,_|_.__/|_|   \__,_|\__\___| 1.0\n",RESET)
    print (BOLD+Red+"Author -----> Himanshu Shukla"+"\n",RESET)

logo()
class keyvalue(argparse.Action): 
    def __call__( self , parser, namespace, 
                 values, option_string = None): 
        setattr(namespace, self.dest, dict())         
        for value in values: 
            key, value = value.split('=') 
            getattr(namespace, self.dest)[key] = value 
counter=0
parser = argparse.ArgumentParser()
req = parser.add_argument_group('Mandatory arguments')
req.add_argument("-u", "--URL", help="Target URL", required=True)
req.add_argument("-w", "--wordlist", help="Wordlist to be used", required=True)
parser.add_argument("-x", "--extensions", help="File Extensions to search for.")
parser.add_argument("-s", "--split", help="Split wordlist into parts & run parallel tasks for faster speed.", type=int)
parser.add_argument("-t", "--timedelay", help="Timedelay between each request.", type=int)
parser.add_argument("-he", "--headers", help="Add Custom Headers to each request.", nargs='*', action = keyvalue)
args = parser.parse_args()

if args.extensions is not None:
    exts = args.extensions.split (",")
else:
    exts = args.extensions

if args.split is not None:
    splt = args.split  
else:
    splt=1




print(BOLD+Yellow+"\n[*] Details About This Session - "+RESET)
print(BOLD+"[*] Target URL : "+str(args.URL))
print("[*] Wordlist : "+str(args.wordlist))
print("[*] Extensions : "+str(args.extensions))
print("[*] Split/Multiprocesses : "+str(splt))
print("[*] Time Delay : "+str(args.timedelay))
print("[*] Headers : "+str(args.headers)+"\n")

def timedel():
    time.sleep(int(args.timedelay))

totallines = sum(1 for line in open(args.wordlist, "r",  encoding="ISO-8859-1"))
if args.extensions is not None:
    extotal=totallines+totallines*len(exts)
else:
    extotal=totallines
print(Blue+"[+] Found Sub-Directories : \n"+RESET)
def dbrute(wordlst):
    
    try:

       with open(wordlst, "r",  encoding="ISO-8859-1") as file:
            counter=0
            
            for value in file:
                counter+=1
                word=value.strip()
                s = requests.Session()
                finalword=args.URL+word

                try:                  
                    payload=s.post(finalword,headers=args.headers)

                    percent=(counter*100*splt)/extotal
                    pal=" [*] Progress : "+str(counter*splt)+"/"+str(extotal)+" "+"["+"{:.2f}".format(percent)+"%"+"]"
                    pal1=len(pal)
                    print(BOLD+Green+pal, end="\r"+RESET)



                    if args.extensions is not None:
                        for k in exts:
                            payload1=s.post(finalword+"."+k,headers=args.headers)
                            counter+=1
                            if not payload1.status_code==404:  
                                pal2="/"+word+"."+k+" : (Response Code "+str(payload1.status_code)+")"
                                pal3=len(pal2)               
                                print(BOLD+pal2+" "*(pal1-pal3))  
                            if args.timedelay is not None:
                                timedel()  
                    if args.timedelay is not None:
                        timedel()
                       
                except:
                    print(BOLD+Red+"[-] Connection Failed With Host!",RESET)
                

                if not payload.status_code==404:  
                    pal2="/"+word+" : (Response Code "+str(payload.status_code)+")"
                    pal3=len(pal2)               
                    print(BOLD+pal2+" "*(pal1-pal3))
                 
                
            print(BOLD+LightGreen+"\n[+] Scanning Finished For "+wordlst+"\n",RESET)

    except:
            print(BOLD+Red+"[-] Something Went Wrong!",RESET)


def splitfile():
    splitLen = totallines/splt
    outputBase = 'part' 
    input = open(args.wordlist, 'r',  encoding="ISO-8859-1").read().split('\n')
    at = 1
    global names
    names=[]
    for lines in range(0, len(input), int(splitLen)):
        outputData = input[lines:lines+int(splitLen)]
        output = open(outputBase + str(at) + '.txt', 'w',  encoding="ISO-8859-1")
        namer=(outputBase + str(at) + '.txt')
        names.append(namer)      
        output.write('\n'.join(outputData))
        output.close()
        at += 1


if __name__ == "__main__":

    splitfile()
    pool = mp.Pool(mp.cpu_count())
    results = pool.map(dbrute, [wordlst for wordlst in names])
    pool.close() 

 

