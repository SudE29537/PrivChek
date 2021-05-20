w = "wordlist.txt"
d = "demofile.txt"

keys = [key for key in (line.strip() for line in open(w)) if key]

with open(d) as f:
    for line in f:
        for key in keys:
            if key in line:
                print(line, end='')
                break