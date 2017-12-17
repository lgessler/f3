#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import os
from f3 import find_freqs


def main():
    if len(sys.argv) != 2:
        print('Usage:\n\tf3 SOURCE DEST')
        exit(1)

    source_path = sys.argv[1]
    dest_path = sys.argv[2]

    if not os.access(source_path, os.R_OK):
        print('File "{0}" does not exist or you lack permission to read it.'.format(source_path))
        exit(1)

    if not os.access(dest_path, os.W_OK):
        print('You do not have permission to write to "{0}"'.format(dest_path))
        exit(1)

    find_freqs(source_path, dest_path)

if __name__ == '__main__':
    main()