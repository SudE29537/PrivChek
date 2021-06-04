import argparse
import os


def parsefile(file):
    keys = [key for key in (line.strip().lower()
                            for line in open(file, encoding="utf-8")) if key]
    return keys


def checkfile(target, ignore, keyword):
    ikeys = parsefile(ignore)
    keys = parsefile(keyword)
    with open(target, encoding="utf-8") as x:
        for lineno, line in enumerate(x):
            for key in keys:
                if key not in ikeys:
                    if key in line.lower():
                        print(
                            f"PII found in file {os.path.abspath(target)}: {key}, line {lineno+1}")


def ckeckdir(target):
    content = os.listdir(target)
    for i in range(0, len(content)):
        if os.path.isfile(content[i]):
            checkfile(content[i], ignorelist, keywordlist)
        else:
            print(
                f"Not working with sub-folders for now. Can not check {content[i]}")


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

ckeckdir(target)
