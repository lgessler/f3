from collections import defaultdict
from bs4 import BeautifulSoup
import enchant
import re


def attempt_parse_html(s):
    return BeautifulSoup(s, "html.parser")


class FilterCounter(object):
    def tokenize_and_count(self, decoded_data, ignore_case):

        en_dict = enchant.Dict("en_GB")
        pattern = r'[^\W\d_]+'

        freqs = defaultdict(int)
        filtered_freqs = defaultdict(int)

        for line in decoded_data.splitlines():
            # strip HTML
            soup = attempt_parse_html(line)
            if bool(soup.find()):
                print("Looks like HTML: \n\t", line)
                line = soup.text
                print("Interpreting as this instead: \n\t", line, "\n")

            english_run = []
            for word in re.findall(pattern, line):
                freqs[word.lower() if ignore_case else word] += 1

                # don't ignore case for the dictionary check
                if en_dict.check(word):
                    english_run.append(word.lower() if ignore_case else word)
                else:
                    if len(english_run) >= 3:
                        for en_word in english_run:
                            filtered_freqs[en_word] += 1
                    english_run = []

            # handle case where run ends at end of line
            if len(english_run) >= 3:
                for en_word in english_run:
                    filtered_freqs[en_word] += 1

        print("Found {0} words, {1} of which looked like English"
              .format(len(freqs), len(filtered_freqs)))

        return freqs, filtered_freqs
