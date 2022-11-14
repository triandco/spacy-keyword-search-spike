# Introduction
This project is a technical spike for blau.

Following [this article](https://towardsdatascience.com/natural-language-processing-document-search-using-spacy-and-python-820acdf604af) to test [Spacy](https://spacy.io) capability to provide search using keywords for text content.


# Requirements
* Python 3.11.0

# Running 
This project use [virtualenv](https://docs.python.org/3/library/venv.html)

```powershell
1. python -m venv env
2. env/Script/active
3. pip install -r requirement.txt
4. py main.py
```

# Conclusion
This is an example of a text search function within a body of text. It does not include indexing.
Searching has two parts:
1. Find similar keywords based on keywords
1. Perform phrase match over a spacy document

Finding similar words implementation is notable:
1. Spacy comes with a large vocabulary of words with its vector representation.
1. Similar words can be found by comparing the distance between vectors. See ```libs.py``` for the implementations:
  1. ```get_similar_words``` behave as lemmatization and stemming, 
  1. ```most_similar``` give word based on meaning.
1. Due to Spacy.PhraseMatcher behavior, it is better to provide case variety of a keyword for better matching results. See ```libs.py``` ```get_case_variety()``` for details.

Bringing spacy across devices might be arduous as there is no out-of-the-box support.
1. https://github.com/explosion/spaCy/issues/4682
1. https://qithub.com/d99kris/spacy-cpp/issues/8
1. https://github.com/ines/spacy-js

There are more straight-forward cross-platform solutions:
1. https://github.com/axa-group/nlp.js
1. https://github.com/NaturalNode/natural
1. https://github.com/winkjs/wink-nlp