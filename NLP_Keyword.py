from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
import pandas as pd

sent_trans = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
keyBERT_model = KeyBERT(model=sent_trans)

data = pd.read_csv('news.csv', encoding='latin-1')


def extract_terms(document, n_gram_range=(3, 3),
                  top_N=15, model=keyBERT_model, diversity_threshold=0.7):
    keywords = model.extract_keywords(document, stop_words='english',
                                      keyphrase_ngram_range=(10, 15),
                                      use_mmr=True,
                                      diversity=diversity_threshold,
                                      top_n=top_N)

    return sorted(keywords, key=lambda tup: (-tup[1], tup[0]))


gold_term = []
gold_term_score = []
silver_term = []
silver_term_score = []
bronze_term = []
bronze_term_score = []

for tweet in data['0']:
    best_terms = extract_terms(tweet)
    print(best_terms)

    gold_term.append(best_terms[0][0])
    gold_term_score.append(best_terms[0][1])

    silver_term.append(best_terms[1][0])
    silver_term_score.append(best_terms[1][1])

    bronze_term.append(best_terms[2][0])
    bronze_term_score.append(best_terms[2][1])

data['gold_term'] = gold_term
data['gold_term_score'] = gold_term_score
data['silver_term'] = silver_term
data['silver_term_score'] = silver_term_score
data['bronze_term'] = bronze_term
data['bronze_term_score'] = bronze_term_score

data.to_csv('test_keywords.csv')

