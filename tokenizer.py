import numpy as np
import pandas as pd

sentence1 = "a book is a good learning resource and is a knowledge system"
sentence2 = "some books are a good learning resource and is a knowledge system"


def sentence_to_vec(sentence, vocab):
    """
    returns matrix where each row is a word and each column
    represents the position of the word in the sentence
    """
    tokens = str.split(sentence)
    tokens_size = len(tokens)
    vocab_size = len(vocab)
    onehot_vectors = np.zeros(vocab_size, int)
    for i, word in enumerate(tokens):
        onehot_vectors[vocab.index(word)] = 1
    return onehot_vectors


vocab = sorted(set(str.split(" ".join([sentence1, sentence2]))))
resp1 = sentence_to_vec(sentence1, vocab)
resp2 = sentence_to_vec(sentence2, vocab)
res = resp1.dot(resp2)
simi = res / len(vocab) * 100
print(f"similarity {simi}")
