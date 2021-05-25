import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="select file or folder to scan. Required",
                    metavar=' ', required=True)
parser.add_argument("-i", "--ignore", help="select ignore file. Default = en-ignore.txt",
                    metavar=' ', default="en-ignore.txt")
parser.add_argument("-k", "--keyword",
                    help="select keyword list. Default = en-keywords.txt", metavar=' ', default="en-keywords.txt")
args = parser.parse_args()
target = args.target
ignorelist = args.ignore
keywordlist = args.keyword

if os.path.isfile(target):

    ikeys = [ikey for ikey in (line.strip().lower()
                               for line in open(ignorelist, encoding="utf-8")) if ikey]

    keys = [key for key in (line.strip().lower()
                            for line in open(keywordlist, encoding="utf-8")) if key]

    with open(target, encoding="utf-8") as x:
        print("File", target)
        for lineno, line in enumerate(x):
            for key in keys:
                if key not in ikeys:
                    if key in line.lower():
                        print(key, lineno+1)

else:
    print("Not working with folder for now.")
