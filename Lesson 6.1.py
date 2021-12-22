import math


class CountVectorizer:
    def __init__(self):
        self.list_of_receipts = []
        self.set_of_words = set()
        self.dict_number_of_words = {}
        self.matrix = []

    def fit_transform(self, input_data):
        for _, string in enumerate(input_data):
            self.list_of_receipts.append(string.lower().split())
            self.set_of_words.update(string.lower().split())
        for word in self.set_of_words:
            self.dict_number_of_words.update({word: []})
        for string in self.list_of_receipts:
            for word in self.dict_number_of_words:
                self.dict_number_of_words[word].append(string.count(word))
        for idx, _ in enumerate(self.list_of_receipts):
            self.matrix.append([elem[idx] for elem in self.dict_number_of_words.values()])
        return self.matrix

    def get_feature_names(self):
        return list(self.dict_number_of_words.keys())


def tf_transform(matrix):
    tf_matrix = []

    for vec in matrix:
        number_of_words = sum(vec)
        tf_matrix_row = [round(word/number_of_words, 3) for word in vec]
        tf_matrix.append(tf_matrix_row)

    return tf_matrix


def idf_transform(matrix):
    result = list()
    document_count = len(matrix) + 1

    for col in range(len(matrix[0])):
        cur_sum = 0
        for row in range(len(matrix)):
            cur_sum += bool(matrix[row][col])
        result.append(cur_sum + 1)

    for i in range(len(result)):
        result[i] = math.log(result[i] / document_count) + 1

    return result


class TfidfTransformer:
    def fit_transform(self, matrix):
        tf = tf_transform(matrix)
        idf = idf_transform(matrix)

        tf_idf = []
        for text in tf:
            tf_idf.append([round(a*b, 3) for a, b in zip(text, idf)])

        return tf_idf


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self._tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
