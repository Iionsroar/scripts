"""Usage: sizes.py <dir>"""

# Note: I now use the software TreeSize

import os
import sys
from contextlib import suppress

# https://ru.stackoverflow.com/questions/461105/%d0%9d%d0%b0%d0%b9%d1%82%d0%b8-%d1%81%d1%83%d0%bc%d0%bc%d0%b0%d1%80%d0%bd%d1%8b%d0%b9-%d1%80%d0%b0%d0%b7%d0%bc%d0%b5%d1%80-%d0%b2%d1%81%d0%b5%d1%85-%d1%80%d0%b5%d0%b3%d1%83%d0%bb%d1%8f%d1%80%d0%bd%d1%8b%d1%85-%d1%84%d0%b0%d0%b9%d0%bb%d0%be%d0%b2-%d0%b2-%d0%ba%d0%b0%d1%82%d0%b0%d0%bb%d0%be%d0%b3%d0%b5-%d1%80%d0%b5%d0%ba%d1%83%d1%80%d1%81%d0%b8%d0%b2%d0%bd%d0%be-%d0%be%d0%b1%d1%85%d0%be%d0%b4%d1%8f-%d0%b2%d1%81%d0%b5/461144#461144
def get_tree_size_scandir(path):
    """Return total size of all regular files in directory tree at *path*."""
    size = 0
    for entry in os.scandir(path):
        with suppress(OSError): # ignore errors for entry & its children
            if entry.is_dir(follow_symlinks=False): # directory
                size += get_tree_size_scandir(entry)
            elif entry.is_file(follow_symlinks=False): # regular file
                size += entry.stat(follow_symlinks=False).st_size
    return size


# https://stackoverflow.com/questions/14996453/python-libraries-to-calculate-human-readable-filesize-from-bytes
suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


# https://stackoverflow.com/questions/48648907/how-do-i-get-the-size-of-sub-directory-from-a-directory-in-python
if len(sys.argv) != 2:
    sys.exit(__doc__)  # print usage

parent_dir = sys.argv[1]
total = 0
for entry in os.scandir(parent_dir):
    if entry.is_dir(follow_symlinks=False): # directory
        size = get_tree_size_scandir(entry)
        # print the size of each immediate subdirectory
        print(humansize(size), entry.name, sep='\t')  
    elif entry.is_file(follow_symlinks=False): # regular file
        size = entry.stat(follow_symlinks=False).st_size
    else:
        continue
    total += size
print(humansize(total), parent_dir, sep='\t') # print the total size for the parent dir
