import argparse
import os

def parsefile(targetfile):
    keys = [key for key in (line.strip().lower() for line in open(targetfile, encoding="utf-8")) if key]
    return keys

def checkfile(targetfile, ignorekeywordlist, keywordlist):
    ikeys = parsefile(ignorekeywordlist)
    keys = parsefile(keywordlist)
    s = True
    with open(targetfile, encoding="utf-8") as x:
        for lineno, line in enumerate(x):
            for key in keys:
                if key not in ikeys:
                    if key in line.lower():
                        if s:
                            print(
                                f"PII found in file {os.path.abspath(targetfile)}")
                            print(f"{key}, line {lineno+1}")
                            s = False
                        else:
                            print(f"{key}, line {lineno+1}")

def checkTarget(target, ignorekeywordlist, keywordlist, ignoretarget):
    itarget = parsefile(ignoretarget)
    with os.scandir(target) as dir:
        for entry in dir:
            if os.path.isdir(entry):
                checkTarget(os.path.abspath(entry),
                                ignorekeywordlist, keywordlist, ignoretarget)
            elif os.path.isfile(entry):
                dirname = os.path.dirname(entry)
                if (os.path.basename(dirname.lower()) not in itarget) and (entry.name not in itarget):
                    checkfile(entry, ignorekeywordlist, keywordlist)

parser = argparse.ArgumentParser()
parser.add_argument("-t ", "--target", help="Select folder to scan. Required",
                    metavar=' ', required=True)
parser.add_argument("-it", "--ignore_target", help="Set ignore target file. Default = ignore_target.txt",
                    metavar=' ', default="Config/ignore_target.txt")
parser.add_argument("-k ", "--keyword",
                    help="Set keyword list file. Default = keywords.txt", metavar=' ', default="Config/keywords.txt")
parser.add_argument("-ik", "--ignore_keyword", help="Set ignore keyword list file. Default = ignore_keyword.txt",
                    metavar=' ', default="Config/ignore_keyword.txt")

args = parser.parse_args()
target = args.target
ignoretarget = args.ignore_target
keyword = args.keyword
ignorekeyword = args.ignore_keyword

checkTarget(target, ignorekeyword, keyword, ignoretarget)