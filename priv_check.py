import argparse

d = "demofile.txt"
i = "ignore.txt"

parser = argparse.ArgumentParser()
# to be used when scan all docs in a folder is created
# parser.add_argument("folder", help="select folder to scan")
parser.add_argument("-t",
                    help="select termlist to use. Default = en-terms.txt", metavar='termlist.txt', default="en-terms.txt")
args = parser.parse_args()
w = args.t

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
