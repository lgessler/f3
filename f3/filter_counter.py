from langid.langid import LanguageIdentifier, model
from collections import defaultdict
from bs4 import BeautifulSoup
import enchant
import re


def attempt_parse_html(s):
    return BeautifulSoup(s, "html.parser")


class FilterCounter(object):
    def __init__(self, target_lang, junk_lang):
        self.target_lang = target_lang
        self.junk_lang = junk_lang

    def detect_most_common_lang(self, lines, identifier):
        counts = defaultdict(int)
        for line in lines:
            lang, _ = identifier.classify(line)
            counts[lang] += 1

        return sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][0]

    def tokenize_and_count(self, decoded_data, ignore_case):
        identifier = LanguageIdentifier.from_modelstring(model,
                                                         norm_probs=True)
        lines = decoded_data.splitlines()

        if self.target_lang is None:
            self.target_lang = self.detect_most_common_lang(lines, identifier)

        identifier.set_languages([self.target_lang, self.junk_lang])

        freqs = defaultdict(int)
        filtered_freqs = defaultdict(int)
        pattern = r'[^\W\d_]+'
        # count = 0
        for line in lines:
            # lang, prob = identifier.classify(line)
            # if not (lang == 'sw' and prob > .99999):
            #    count += 1
                # print()
                # print(line)
                # print(lang, prob)
            soup = attempt_parse_html(line)
            if bool(soup.find()):
                print("Looks like HTML: \n\t", line)
                line = soup.text
                print("Interpreting as this instead: \n\t", line, "\n")

            for word in re.findall(pattern, line):
                if ignore_case:
                    word = word.lower()
                # if lang == self.target_lang:
                if True:
                    freqs[word] += 1
                else:
                    filtered_freqs[word] += 1

        en_dict = enchant.Dict("en_US")
        print("Found {0} words, {1} of which were filtered out"
              .format(len(freqs),
                      len([x for x, _ in freqs.items()
                           if en_dict.check(x)])))
        for word, freq in \
                sorted(freqs.items(), reverse=True, key=lambda x: x[1]):
            if en_dict.check(word):
                filtered_freqs[word] += freqs[word]
                freqs.pop(word)

        return freqs, filtered_freqs

