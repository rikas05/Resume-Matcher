# 🧠 AI-Powered Resume Matcher

An intelligent resume matching system that uses **Sentence-BERT embeddings** and **cosine similarity** to compare resumes against job descriptions. It evaluates each candidate based on **match score**, **percentile ranking**, and supports **shortlisting**, **filtering**, and **exporting** results.

---

## 🚀 Features

- 🔍 Automatically extracts and cleans text from PDF resumes  
- 🧠 Uses Sentence-BERT (`all-MiniLM-L6-v2`) for semantic matching  
- 📊 Calculates cosine similarity and percentile ranks  
- 🎯 Filters candidates based on customizable thresholds  
- 📝 Exports shortlisted results to a text file  
- 📂 Easily pluggable for recruiters or job portals

---

## 📁 Project Structure

resume-matcher-ai/
│
├── main.py # Main script to run the matcher
├── resume_matcher.py # Contains ResumeMatcherAI class and logic
├── resumes/ # Folder to store PDF resumes
│ └── *.pdf # (Add your resume files here)
├── job_description.pdf # (Optional) Job description in PDF
├── shortlisted_candidates.txt # Auto-generated if export is enabled
└── README.md # Project documentation


---

## 🧰 Requirements

Install dependencies using pip:

```bash
pip install sentence-transformers scikit-learn scipy numpy pypdf

    ✅ Compatible with both pypdf and PyPDF2. Defaults to PyPDF2.

🛠️ How to Use

    Add Resumes
    Place your resume PDFs inside the resumes/ folder.

    Run the Application

python main.py

    Provide Job Description

        Option 1: Type or paste it manually
        ⚠️ When pasting a job description manually, make sure to paste it as one single line (no line breaks) for best results.

        Option 2: Place a file named job_description.pdf in the root directory and choose to load it.

    Set Shortlisting Criteria

        Enter minimum match score and percentile ranking to filter candidates.

    View Results

        See a ranked list of candidates with match scores and percentile rankings.

    Export Results (Optional)

        Choose to export shortlisted candidates to shortlisted_candidates.txt.

📊 Example Output

RESUME MATCHING RESULTS
================================================================================
Rank   Filename                      Match Score   Percentile   Status      
--------------------------------------------------------------------------------
1      John_Smith.pdf               88.5%         97.5%        SHORTLISTED
2      Alice_Johnson.pdf            79.2%         85.1%        SHORTLISTED
3      Mark_Taylor.pdf              52.0%         40.0%        FILTERED OUT