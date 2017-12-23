from collections import defaultdict
from bs4 import BeautifulSoup
import enchant
import re


def attempt_parse_html(s):
    return BeautifulSoup(s, "html.parser")


class FilterCounter(object):
    def tokenize_and_count(self, decoded_data, ignore_case):
        lines = decoded_data.splitlines()

        freqs = defaultdict(int)
        filtered_freqs = defaultdict(int)
        pattern = r'[^\W\d_]+'
        for line in lines:
            soup = attempt_parse_html(line)
            if bool(soup.find()):
                print("Looks like HTML: \n\t", line)
                line = soup.text
                print("Interpreting as this instead: \n\t", line, "\n")

            for word in re.findall(pattern, line):
                if ignore_case:
                    word = word.lower()
                freqs[word] += 1

        en_dict = enchant.Dict("en_US")
        for word, freq in \
                sorted(freqs.items(), reverse=True, key=lambda x: x[1]):
            if en_dict.check(word):
                filtered_freqs[word] += freqs[word]

        print("Found {0} words, {1} of which were filtered out"
              .format(len(freqs), len(filtered_freqs)))

        return freqs, filtered_freqs
