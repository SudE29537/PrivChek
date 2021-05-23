import configparser
import argparse

config = configparser.ConfigParser()
config.read('config.ini')

w = config['DEFAULT']['termfile']
d = "demofile.txt"
i = "ignore.txt"

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--termlist", help="select termlist to use")
args = parser.parse_args()

if args.termlist:
    w = args.termlist

ikeys = [ikey for ikey in (line.strip().lower()
                           for line in open(i, encoding="utf-8")) if ikey]

keys = [key for key in (line.strip().lower()
                        for line in open(w, encoding="utf-8")) if key]

with open(d, encoding="utf-8") as f:
    print("File", d)
    for lineno, line in enumerate(f):
        for key in keys:
            if key not in ikeys:
                if key in line.lower():
                    print(key, lineno+1)
