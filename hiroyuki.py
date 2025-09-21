import random
from janome.tokenizer import Tokenizer

class MarkovChain:
    def __init__(self, n=2):
        self.n = n
        self.model = {}

    def train(self, text):
        t = Tokenizer()
        tokens = [token.surface for token in t.tokenize(text)]
        for i in range(len(tokens) - self.n):
            key = tuple(tokens[i:i+self.n])
            next_word = tokens[i+self.n]
            if key not in self.model:
                self.model[key] = []
            self.model[key].append(next_word)

    def generate(self, length=30):
        key = random.choice(list(self.model.keys()))
        result = list(key)
        for _ in range(length - self.n):
            next_words = self.model.get(key)
            if not next_words:
                break
            next_word = random.choice(next_words)
            result.append(next_word)
            key = tuple(result[-self.n:])
        return ''.join(result)

if __name__ == "__main__":
    with open("hiroyuki.txt", encoding="utf-8") as f:
        text = f.read()

    mc = MarkovChain(n=2)
    mc.train(text)

    print(mc.generate(30))