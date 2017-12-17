#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import argparse
import time
import sys
from f3.regex_counter import RegexCounter

try:
    from chardet.universaldetector import UniversalDetector
except ImportError:
    print('WARNING: failed to load package "chardet". '
          'Assuming the file is UTF-8 encoded.')
    time.sleep(1)

SUPPORTED_ENCODINGS = ['windows-1252', 'ISO-8859-1', 'ascii',
                       'utf-8', 'utf-16', 'utf-32']


def _detect_encoding(source_path):
    '''Use the chardet library to make a guess at the encoding.
    See http://chardet.readthedocs.io/en/latest/usage.html '''
    infile = open(source_path, 'rb')
    detector = UniversalDetector()
    for line in infile.readlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    infile.close()
    result = detector.result

    print('Input file is encoded using {0} with confidence {1}'
          .format(result['encoding'], result['confidence']))
    return result['encoding'], result['confidence']


def _choose_encoding(source_path):
    if 'chardet' in sys.modules:
        encoding, confidence = _detect_encoding(source_path)
    else:
        encoding = "UTF-8"

    while encoding not in SUPPORTED_ENCODINGS:
        print('Encoding {0} is not supported. '
              'Enter a supported encoding to continue, '
              'or press ENTER to exit.'.format(encoding))
        print('Supported encodings: ' + ', '.join(SUPPORTED_ENCODINGS))
        entry = input('\n')
        if entry == "":
            sys.exit(0)
        encoding = entry

    return encoding


def _transcode(raw_data, encoding):
    '''See: https://docs.python.org/3/library/codecs.html#standard-encodings '''
    encoding = encoding.lower()
    if encoding == 'ascii':
        return raw_data.decode('ascii').encode('utf-8')

    if encoding == 'windows-1252':
        return raw_data.decode('windows-1252').encode('utf-8')

    if encoding == 'iso-8859-1':
        return raw_data.decode('iso-8859-1').encode('utf-8')

    if encoding == 'utf-16':
        return raw_data.decode('utf-16').encode('utf-8')

    if encoding == 'utf-32':
        return raw_data.decode('utf-32').encode('utf-8')

    return raw_data


def find_freqs(source_path, dest_path, opts={}):
    with open(source_path, 'rb') as infile:
        raw_data = infile.read()

    encoding = _choose_encoding(source_path)
    transcoded_data = _transcode(raw_data, encoding)

    counter = RegexCounter()
    freqs = counter.tokenize_and_count(transcoded_data,
                                       opts['ignore_case'])

    with open(dest_path, 'w', encoding='utf-8') as outfile:
        for word, freq in sorted(freqs.items(),
                                 key=lambda x: x[1],
                                 reverse=True):
            outfile.write("{0}\t{1}\n".format(word, freq))
    print("Wrote to {0} successfully".format(dest_path))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='text file')
    parser.add_argument('dest', help='the TSV file frequencies will be written to')
    parser.add_argument('-i', '--ignore-case', action="store_true", default=False,
                        help='ignore case for determining word equivalence')

    args = parser.parse_args()

    source_path = args.source
    dest_path = args.dest

    if not os.access(source_path, os.R_OK):
        print('File "{0}" does not exist or you lack permission to read it.'
              .format(source_path))
        exit(1)

    find_freqs(source_path, dest_path, vars(args))

if __name__ == '__main__':
    main()


