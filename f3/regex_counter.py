from collections import defaultdict
import re


class RegexCounter(object):
    def tokenize_and_count(self, data, ignore_case):
        freqs = defaultdict(int)
        s = data.decode('utf-8')
        pattern = r'\w+'
        for word in re.findall(pattern, s):
            if ignore_case:
                word = word.lower()
            freqs[word] += 1

        return freqs
