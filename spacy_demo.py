import spacy

nlp = spacy.load('en_core_web_sm')


def resolve(sentence):
    doc = nlp(sentence)

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)


resolve("ofer please give me information about restaurant sales")
