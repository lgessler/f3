import time
import sys
from transcode import transcode, SUPPORTED_ENCODINGS
try:
    from chardet.universaldetector import UniversalDetector
except ImportError:
    print('WARNING: failed to load package "chardet". Assuming the file is UTF-8 encoded.')
    time.sleep(1)


def _detect_encoding(lines):
    '''Use the chardet library to make a guess at the encoding.'''
    detector = UniversalDetector()
    for line in lines:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    result = detector.result
    print('File is encoded using {0} with confidence {1}'.format(result.encoding, result.confidence))
    return result.encoding

def _choose_encoding(lines):
    if 'chardet' in sys.modules:
        encoding = _detect_encoding(lines)
    else:
        encoding = "UTF-8"

    while encoding not in SUPPORTED_ENCODINGS:
        print('Encoding {0} is not supported. '
              'Enter a supported encoding to continue, or press ENTER to exit.'.format(encoding))
        print('Supported encodings: ' + ', '.join(SUPPORTED_ENCODINGS))
        entry = input('\n')
        if entry == "":
            sys.exit(0)
        encoding = entry

    return encoding

def find_freqs(source_path, dest_path):
    with open(source_path) as infile:
        rawdata = infile.read()
        lines = infile.readlines()

    encoding = _choose_encoding(lines)
    transcoded_lines = transcode(lines, encoding)


