# 🧠 Smart Resume Matcher

This is an NLP-powered tool that compares a resume (PDF) with a job description (text file) and returns a similarity percentage and keyword analysis.

---

## 📦 Features

- ✅ PDF text extraction using `pdfminer.six`
- ✅ NLP preprocessing: lowercasing, punctuation removal, stopwords
- ✅ Word2Vec-based embedding & cosine similarity
- ✅ Keyword match and gap analysis
- ✅ Modular design with CLI interface

---

## 🚀 How to Use

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/resume-matcher.git
cd resume-matcher
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```
## 🔁 Sample Files

Replace these files with your own resume and job description(keep the names same so as to avoid error):

- `sample_resume.pdf`
- `sample_jd.txt`

### 3. Run the matcher

```bash
python main.py --resume sample_resume.pdf --jd sample_jd.txt
```

Or use your own files:

```bash
python main.py --resume path/to/your_resume.pdf --jd path/to/job_desc.txt
```

---



---

## 🧪 Output Example

```
🔍 Match Percentage: 78.56%

✅ Matched Keywords:
python, nlp, machine, learning, word2vec

❌ Missing Keywords:
spacy, tfidf, gensim, lemmatization
```

---

## 🛠 Technologies Used

- Python 3
- PDFMiner (for PDF text extraction)
- NLTK (tokenization, stopwords)
- Gensim (Word2Vec)
- Scikit-learn (cosine similarity)
- SymSpell (spelling correction - optional)

---

## 📁 Project Structure

```
resume-matcher/
├── main.py
├── resume_matcher.py
├── requirements.txt
├── README.md
├── sample_resume.pdf
└── sample_jd.txt
```

---

## 📄 License

MIT License — free to use, share, and modify.

---

## 👨‍💻 Author

Rikas Mohammed N
