

import argparse
from resume_matcher import extract_text_from_pdf, run_matcher

parser = argparse.ArgumentParser(description="Resume Matcher")
parser.add_argument('--resume', type=str, required=True, help='Path to resume PDF')
parser.add_argument('--jd', type=str, required=True, help='Path to job description TXT')
args = parser.parse_args()

resume_text = extract_text_from_pdf(args.resume)

with open(args.jd, 'r', encoding='utf-8') as f:
    jd_text = f.read()

run_matcher(resume_text, jd_text)