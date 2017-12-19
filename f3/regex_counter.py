from collections import defaultdict
import re


class RegexCounter(object):
    def tokenize_and_count(self, decoded_data, ignore_case):
        freqs = defaultdict(int)
        pattern = r'\w+'
        for word in re.findall(pattern, decoded_data):
            if ignore_case:
                word = word.lower()
            freqs[word] += 1

        return freqs
