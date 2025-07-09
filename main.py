# main.py

from resume_matcher import ResumeMatcherAI, export_shortlisted_candidates

def main():
    """
    Main function to run the AI-powered resume matcher.
    """
    print("="*60)
    print("         AI-Powered Resume Matcher")
    print("="*60)

    # Initialize the ResumeMatcherAI class
    matcher = ResumeMatcherAI()

    # Match resumes against job description
    results, shortlisted, min_match_score, min_percentile = matcher.match_resumes()

    # Display matching results
    matcher.display_results(results, shortlisted, min_match_score, min_percentile)

    # Export shortlisted candidates if any
    if shortlisted:
        print("\nWould you like to export shortlisted candidates to a file?")
        export_choice = input("Enter 'y' to export or any other key to skip: ").strip().lower()
        if export_choice == 'y':
            export_shortlisted_candidates(shortlisted)

if __name__ == "__main__":
    main()
