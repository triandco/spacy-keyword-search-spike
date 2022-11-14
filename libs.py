import enchant
from scipy import spatial
import numpy
import spacy

def flatten(l):
    return [item for sublist in l for item in sublist]


def distinct(a):
    return list(set(a))


def cosineSimilarity(vect1, vect2):
    return 1 - spatial.distance.cosine(vect1, vect2)


def get_case_variety(word):
    return distinct([word.upper(), word.lower(), word.title(), word])


def read_file(path):
    content = ''
    # ignore emoji
    with open(path, encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        content = '\n'.join(lines)

    return content


# find most similar word using an nlp vocabulary
# 'extending' would return ['there', 'and', 'extending', 'extend']
def get_similar_words(keyword, nlp=spacy.load('en_core_web_lg')):
    similarity_list = []

    keyword_vector = nlp(keyword).vector

    for tokens in nlp.vocab:
        if (tokens.has_vector):
            if (tokens.is_lower):
                if (tokens.is_alpha):
                    similarity_list.append((tokens, cosineSimilarity(keyword_vector, tokens.vector)))

    similarity_list = sorted(similarity_list, key=lambda item: -item[1])
    similarity_list = similarity_list[:30]

    top_similar_words = [item[0].text for item in similarity_list]

    top_similar_words = top_similar_words[:3]
    top_similar_words.append(keyword)

    for token in nlp(keyword):
        top_similar_words.insert(0, token.lemma_)

    for words in top_similar_words:
        if words.endswith("s"):
            top_similar_words.append(words[0:len(words)-1])

    top_similar_words = list(set(top_similar_words))

    top_similar_words = [words for words in top_similar_words if enchant.Dict("en_US").check(words) == True]
    
    return top_similar_words


# find most similar word using an nlp vocabulary
# 'extending' would return ['extending', 'overextending', 'extends', 'extenuating', 'Extending', 'extended', 'extendible', 'wending', 'terminating', 'lengthening']
def most_similar(word, nlp=spacy.load('en_core_web_lg')):
    ms = nlp.vocab.vectors.most_similar(
        numpy.asarray([nlp.vocab.vectors[nlp.vocab.strings[word]]]), n=10)
    words = [nlp.vocab.strings[w] for w in ms[0][0]]
    return words