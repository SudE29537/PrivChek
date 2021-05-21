w = "wordlist.txt"
d = "demofile.txt"

keys = [key for key in (line.strip().lower() for line in open(w)) if key]

with open(d) as f:
    print("File", w)
    for lineno, line in enumerate(f):
        # for line in f:
        for key in keys:
            if key in line.lower():
                print(key, lineno+1)
