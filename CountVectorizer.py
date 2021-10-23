class CountVectorizer:
    def __init__(self):
        self.texts = list()
        self.dictionary = dict()
        self.matrix = []

    def fit_transform(self, receipts):
        for idx, string in enumerate(receipts):
            self.texts.append(string.lower().split(" "))
        self.dictionary = dict((elem, []) for elem in set([word for element in self.texts for word in element]))
        for string in self.texts:
            for word in self.dictionary:
                self.dictionary[word].append(string.count(word))
        for i in range(len(self.texts)):
            self.matrix.append([elem[i] for elem in self.dictionary.values()])
        return self.matrix

    def get_feature_names(self):
        return list(self.dictionary.keys())
