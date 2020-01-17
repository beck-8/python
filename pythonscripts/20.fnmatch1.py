import fnmatch
import os

# linux command: find
for file in os.listdir("files"):
    if fnmatch.fnmatch(file, "*.jpg"):
        print(os.path.abspath("file"))




