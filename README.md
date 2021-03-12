# dbrute : Sub-Directory Brute-Forcing Tool

dbrute is a powerful tool made with python3. It is mainly used for Sub-Directory Brute Forcing.

It supports custom extentions search, custom headers, time delays, Splitting wordlist into parts & Parallel Processing.

The Unique Feature of dbrute is it can split any given wordlist into specific number of parts and then use all those parts to launch parallel processes for each part.
This will increase the efficienty of the attack by high amount.


## How To Install :  

```
git clone https://github.com/etc5had0w/dbrute.git
cd dbrute/
ln -s ${PWD}/dbrute.py /usr/bin/dbrute
```

## How To Use :

run this commands from your terminal to view help page:

```
$dbrute -h


usage: dbrute [-h] -u URL -w WORDLIST [-x EXTENTIONS] [-s SPLIT] [-t TIMEDELAY] [-he [HEADERS ...]]

optional arguments:
  -h, --help            show this help message and exit
  -x EXTENTIONS, --extentions EXTENTIONS
                        File Extentions to search for.
  -s SPLIT, --split SPLIT
                        Split wordlist into parts & run parallel tasks for faster speed.
  -t TIMEDELAY, --timedelay TIMEDELAY
                        Timedelay between each request.
  -he [HEADERS ...], --headers [HEADERS ...]
                        Add Custom Headers to each request.

Mandatory arguments:
  -u URL, --URL URL     Target URL
  -w WORDLIST, --wordlist WORDLIST
                        Wordlist to be used

```

## Example Usage

Basic Usage With Wordlist and URL :

```
dbrute -u 192.168.1.2 -w /path/to/wordlist.txt
```

Using Extentions :

```
dbrute -u 192.168.1.2 -w /path/to/wordlist.txt -x php,txt,html,asp
```

Using Split/ Parallel Processing Function :

(the number of -s is the total number of parallel processes and  splitted parts of wordlist.)

```
dbrute -u 192.168.1.2 -w /path/to/wordlist.txt -s 6
```

Using Custom Headers :

```
dbrute -u 192.168.1.2 -w /path/to/wordlist.txt -he User-agent=Mozilla cookie=3495tu39thj3459thj9th
```

Using Time Delay (in seconds) :

```
dbrute -u 192.168.1.2 -w /path/to/wordlist.txt -t 1
```

## Features :

dbrute Supports These Features :

* Basic Sub-Directory Busting Using Wordlist
* Searching For Files With Specific Extentions
* Splitting the wordlist into specific number of parts and launch parallel processing attack.
* Adding Time Delays Between Each Request.
* Adding Custom Headers.


## Disclaimer

Use this tool on your own risk. Creator of this tool will not be held responsible for any harm caused by usage of this tool.

