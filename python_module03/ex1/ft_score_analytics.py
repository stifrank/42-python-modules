print("=== Score Analytics System ===")

score_input = "120,85,90,invalid,100,75"
print(f"Processing scores: {score_input}")

parts = score_input.split(",")

valid_scores = []
invalid_entries = 0

for p in parts:
    try:
        score = int(p)
        valid_scores.append(score)
    except ValueError:
        print(f"Invalid entry skipped: {p}")
        invalid_entries += 1

if len(valid_scores) > 0:
    total_scores = len(valid_scores)
    average = sum(valid_scores) / total_scores
    highest = max(valid_scores)
    lowest = min(valid_scores)

    print("=== Score Statistics ===")
    print(f"Valid scores: {valid_scores}")
    print(f"Average score: {average}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
else:
    print("No valid scores found.")

print("=== Processing Summary ===")
print(f"Valid entries: {len(valid_scores)}")
print(f"Invalid entries: {invalid_entries}")
