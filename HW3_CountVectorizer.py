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


if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
