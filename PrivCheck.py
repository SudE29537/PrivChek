w = "wordlist.txt"
d = "demofile.txt"

keys = [key for key in (line.strip().lower()
                        for line in open(w, encoding="utf-8")) if key]

with open(d, encoding="utf-8") as f:
    print("File", d)
    for lineno, line in enumerate(f):
        for key in keys:
            if key in line.lower():
                print(key, lineno+1)
