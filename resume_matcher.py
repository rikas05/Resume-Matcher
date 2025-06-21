

import re
import string
from pdfminer.high_level import extract_text
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from symspellpy.symspellpy import SymSpell, Verbosity
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

resume_text = extract_text_from_pdf("sample_resume.pdf")
with open('sample_jd.txt', 'r',encoding="utf-8") as file:
    job_desc_text = file.read()

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
sym_spell.load_dictionary("frequency_dictionary_en_82_765.txt", term_index=0, count_index=1)

def correct_spelling(text):
    suggestions = sym_spell.lookup_compound(text, max_edit_distance=2)
    return suggestions[0].term if suggestions else text

def preprocess(text):
    text = text.lower()
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    text = correct_spelling(" ".join(tokens))
    return text, tokens
clean_resume, resume_tokens = preprocess(resume_text)
clean_jd, jd_tokens = preprocess(job_desc_text)

corpus = [resume_tokens, jd_tokens]
model = Word2Vec(corpus, vector_size=100, window=5, sg=1, min_count=1)

def average_vector(tokens, model):
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

resume_vec = average_vector(resume_tokens, model)
jd_vec = average_vector(jd_tokens, model)

similarity = cosine_similarity([resume_vec], [jd_vec])[0][0]
match_percentage = round(similarity * 100, 2)

resume_set = set(resume_tokens)
jd_set = set(jd_tokens)

matched = jd_set & resume_set
missing = jd_set - resume_set

print("📊 Resume–Job Match Score:", match_percentage, "%\n")
print("✅ Matched Keywords:", ", ".join(sorted(matched)))
print("\n❌ Missing Keywords:", ", ".join(sorted(missing)))

