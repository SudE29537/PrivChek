import argparse
import os


def parsefile(targetFile):
    keys = [key for key in (line.strip().lower()
                            for line in open(targetFile, encoding="utf-8")) if key]
    return keys


def checkfile(targetFile, ignoreKeywordList, keywordList):
    ikeys = parsefile(ignoreKeywordList)
    keys = parsefile(keywordList)
    s = True
    with open(targetFile, encoding="utf-8") as x:
        for lineno, line in enumerate(x):
            for key in keys:
                if key not in ikeys:
                    if key in line.lower():
                        if s:
                            print(
                                f"PII found in file {os.path.abspath(targetFile)}")
                            print(f"{key}, line {lineno+1}")
                            s = False
                        else:
                            print(f"{key}, line {lineno+1}")


def checkTarget(target, ignoreKeywordList, keywordList):
    with os.scandir(target) as dir:
        for entry in dir:
            if entry.name not in ignoreTarget:
                if os.path.isdir(entry):
                    checkTarget(os.path.abspath(entry),
                                ignoreKeywordList, keywordList)
                elif os.path.isfile(entry):
                    checkfile(entry, ignoreKeywordList, keywordList)


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="select file or folder to scan. Required",
                    metavar=' ', required=True)
parser.add_argument("-i", "--ignore", help="select ignore file. Default = en-ignore.txt",
                    metavar=' ', default="Default/en-ignore.txt")
parser.add_argument("-k", "--keyword",
                    help="select keyword list. Default = en-keywords.txt", metavar=' ', default="Default/en-keywords.txt")
args = parser.parse_args()
target = args.target
ignorelist = args.ignore
keywordlist = args.keyword
ignoreTarget = parsefile("Default/ignore-target.txt")

checkTarget(target, ignorelist, keywordlist)
