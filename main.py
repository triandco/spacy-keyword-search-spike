import spacy
from spacy.matcher import PhraseMatcher
import uuid
from libs import get_similar_words, read_file, flatten, get_case_variety

def search_for_keyword(keywords, doc_obj, nlp):
    matcher = PhraseMatcher(nlp.vocab)
    phrase_list = [nlp(word) for word in keywords]
    matcher.add(str(uuid.uuid4()), phrase_list)
    doc = nlp(doc_obj)
    matched_items = matcher(doc)

    matched_text = []
    for match_id, start, end in matched_items:
        span = doc[start: end]
        matched_text.append(span.sent.text)

    return matched_text


if __name__ == "__main__":
    keyword = 'extending'
    input_file = 'docs/test.txt'
    nlp = spacy.load('en_core_web_lg')
    similar = get_similar_words(keyword, nlp)
    print(similar)
    keywords = flatten([get_case_variety(word) for word in similar])
    main_doc = nlp(read_file(input_file))
    result = search_for_keyword(keywords, main_doc, nlp)

    print("result: ")
    print(result)
