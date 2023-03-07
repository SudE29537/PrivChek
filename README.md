# PrivChek
### Privacy Check for DevSecOps
---
The tool will search for common PII (Personally Identifiable Information) in your code, to help you comply with privacy laws and regulations.

usage: priv_check.py [-h] -t [-it ] [-k  ] [-ik ]

options:
  -h  , --help            Show this help message and exit
  -t  , --target          Select folder to scan. Required
  -it , --ignore_target   Set ignore target file. Default = ignore_target.txt
  -k  , --keyword         Set keyword list file. Default = keywords.txt
  -ik , --ignore_keyword  Set ignore keyword list file. Default = ignore_keyword.txt

Lists are not case sensitive.

Ignore target will ignore files and folders. 

---
The project is in its early stages. Feel free to collaborate.