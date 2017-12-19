from langid.langid import LanguageIdentifier, model
from collections import defaultdict
import re


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
        pattern = r'\w+'
        for line in lines:
            lang, _ = identifier.classify(line)

            for word in re.findall(pattern, line):
                if ignore_case:
                    word = word.lower()
                if lang == self.target_lang:
                    freqs[word] += 1
                else:
                    filtered_freqs[word] += 1

        return freqs, filtered_freqs
