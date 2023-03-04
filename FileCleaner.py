# Name      : FileCleaner
# Version   : v1.01
# Author    : M. Vlaanderen
# Date      : 2022/06/16
# ========================================
# Changelog
# ========================================
# v1.0  - First commit
# v1.1  - Added exception handling
# ========================================

import os
import datetime
import glob
import sys


if len(sys.argv) < 2:
    print("Missing arguments. Use like this: 'cleaner.py [path] [days]'")
    print("Example: cleaner.py /foo/bar/ 7")
    exit(1)

path = sys.argv[1]
retention = sys.argv[2]
today = datetime.datetime.today()
os.chdir(path)

for root, directories, files in os.walk(path, topdown=False):
    for name in files:
        t = os.stat(os.path.join(root, name))[8]
        filetime = datetime.datetime.fromtimestamp(t) - today
        if filetime.days <= -int(retention):
            os.remove(os.path.join(root, name))