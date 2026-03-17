import argparse

def calculate_v2c(revenue, savings, complexity, scarcity):
    """
    Calculates the Value-to-Company (V2C) score.
    
    Inputs:
    - revenue: Annual revenue generated or influenced by the candidate ($).
    - savings: Annual costs saved through optimizations ($).
    - complexity: Role complexity factor (1: Low, 5: Expert).
    - scarcity: Skill scarcity in the market (1: Abundant, 5: Unicorn).
    """
    base_value = revenue + savings
    multiplier = (complexity * 0.5) + (scarcity * 0.5)
    v2c_score = base_value * multiplier
    return v2c_score

def main():
    parser = argparse.ArgumentParser(description="Value-to-Company (V2C) ROI Estimator")
    parser.add_argument("-r", "--revenue", type=float, default=0, help="Revenue Generated ($)")
    parser.add_argument("-s", "--savings", type=float, default=0, help="Cost Savings ($)")
    parser.add_argument("-c", "--complexity", type=int, choices=range(1, 6), default=3, help="Complexity (1-5)")
    parser.add_argument("-k", "--scarcity", type=int, choices=range(1, 6), default=3, help="Scarcity (1-5)")

    args = parser.parse_args()

    score = calculate_v2c(args.revenue, args.savings, args.complexity, args.scarcity)

    print("\n--- Value-to-Company (V2C) Analysis ---")
    print(f"Calculated ROI Value: ${score:,.2f}")
    
    # Heuristic for salary estimation (typically 20-40% of generated value for high-impact roles)
    low_bound = score * 0.15
    high_bound = score * 0.35
    
    print(f"Recommended Annual Comp Target: ${low_bound:,.2f} - ${high_bound:,.2f}")
    print("Note: This is a tactical estimate based on proven STAR metrics.")

if __name__ == "__main__":
    main()
