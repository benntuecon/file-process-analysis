import heapq
from collections import defaultdict
from typing import Callable

# uncomment this for the first time run
# nltk.download('stopwords')
from nltk.corpus import stopwords

# load the stopwords and turn it into a hash-set for better performance check existence check
stopwords_set = set(stopwords.words('english'))


# You can call the function like this:
# for word, count in get_top_k_words('../dataset/data_2.5GB.txt', 10):
#     logging.info(f'{word}: {count:-20}')


class BaselineSolution:

    def read_file(self, f):
        """
        Lazy function (generator) to read a file piece by piece.
        return a single chunk of data
        """
        while True:
            data = f.read()
            if not data:
                break
            yield data

    @staticmethod
    def count_words(word_counts, words):
        for word in words:
            word_counts[word] += 1

    @staticmethod
    def sorting(k, word_counts):
        return heapq.nlargest(
            k, word_counts.items(), key=lambda i: i[1])

    def top_k(self, file_name, k=10):
        word_counts = defaultdict(int)
        with open(file_name, 'r') as f:
            for piece in self.read_file(f):
                piece = piece.lower()
                words = [word for word in piece.split(
                ) if word not in stopwords_set]
                self.count_words(word_counts, words)
        # get top k words
        top_k = self.sorting(k, word_counts)
        return top_k


base_solver = BaselineSolution()
