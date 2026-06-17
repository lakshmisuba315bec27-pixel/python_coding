from collections import Counter
try:
    N = int(input("Enter number of lines: ").strip())
except ValueError:
    print("Please enter a valid number.")
    exit()

for i in range(N):
    line = input().strip()
    if not line:
        continue
        
    counts = Counter(line)
    max_count = max(counts.values())
    
    winners = [char for char, count in counts.items() if count == max_count]

    upper_winners = sorted([c for c in winners if c.isupper()])
    lower_winners = sorted([c for c in winners if c.islower()])
    
    # 6. Print the formatted result
    result = "".join(upper_winners + lower_winners)
    print(result)
