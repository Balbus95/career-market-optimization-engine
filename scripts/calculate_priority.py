import argparse

def calculate_priority(importance, frequency, current_level):
    """
    Calculates the priority score P for a skill gap.
    Formula: P = (Importance * Frequency) - Current Level
    
    Scale (1-5):
    - Importance: How critical is this skill for the target role?
    - Frequency: How often is this skill used in the role?
    - Current Level: Candidate's current proficiency.
    """
    priority = (importance * frequency) - current_level
    return priority

def main():
    parser = argparse.ArgumentParser(description="Career Skill Gap Priority Calculator")
    parser.add_argument("-i", "--importance", type=int, required=True, help="Importance (1-5)")
    parser.add_argument("-f", "--frequency", type=int, required=True, help="Frequency (1-5)")
    parser.add_argument("-l", "--level", type=int, required=True, help="Current Level (1-5)")

    args = parser.parse_args()

    p_score = calculate_priority(args.importance, args.frequency, args.level)

    print(f"
--- Skill Gap Analysis ---")
    print(f"Priority Score (P): {p_score}")
    
    if p_score >= 20:
        print("Status: CRITICAL GAP. Immediate upskilling required.")
    elif p_score >= 15:
        print("Status: HIGH PRIORITY. Focus on this in the next quarter.")
    elif p_score >= 10:
        print("Status: MODERATE. Monitor and improve when possible.")
    else:
        print("Status: LOW PRIORITY/STRENGTH. Maintain current level.")

if __name__ == "__main__":
    main()
