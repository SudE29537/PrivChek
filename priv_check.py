import argparse
import os

def parsefile(targetfile):
    keys = [key for key in (line.strip().lower() for line in open(targetfile, encoding="utf-8")) if key]
    return keys

def checkfile(targetfile):
    ikeys = parsefile(ignorekeywords)
    keys = parsefile(keywords)
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

def checkTarget(target, ignoretarget, extensions, ignoreextensions):
    itarget = parsefile(ignoretarget)
    ext = parsefile(extensions)
    iextensions = parsefile(ignoreextensions)
    with os.scandir(target) as dir:
        for entry in dir:
            if os.path.isdir(entry):
                checkTarget(os.path.abspath(entry),
                                 ignoretarget, extensions, ignoreextensions)
            elif os.path.isfile(entry):
                dirname = os.path.dirname(entry)
                if (os.path.basename(dirname.lower()) not in itarget) and (entry.name not in itarget) and (os.path.splitext(entry)[1] not in iextensions) and (os.path.splitext(entry)[1] in ext):
                    checkfile(entry)

parser = argparse.ArgumentParser()
parser.add_argument("-t ", "--target", help="Select target folder to scan. Required",
                    metavar=' ', required=True)
parser.add_argument("-it", "--ignore_targets", help="Set ignore targets file. Default = ignore_targets.txt",
                    metavar=' ', default="Config/ignore_targets.txt")
parser.add_argument("-k ", "--keywords",
                    help="Set keyword list file. Default = keywords.txt", metavar=' ', default="Config/keywords.txt")
parser.add_argument("-ik", "--ignore_keywords", help="Set ignore keywords list file. Default = ignore_keywords.txt",
                    metavar=' ', default="Config/ignore_keywords.txt")
parser.add_argument("-e ", "--extensions",
                    help="Set file extensions list file. Default = extensions.txt", metavar=' ', default="Config/extensions.txt")
parser.add_argument("-ie", "--ignore_extensions", help="Set ignore extensions list file. Default = ignore_extensions.txt",
                    metavar=' ', default="Config/ignore_extensions.txt")

args = parser.parse_args()
target = args.target
ignoretargets = args.ignore_targets
keywords = args.keywords
ignorekeywords = args.ignore_keywords
extensions = args.extensions
ignoreextensions = args.ignore_extensions

checkTarget(target, ignoretargets, extensions, ignoreextensions)