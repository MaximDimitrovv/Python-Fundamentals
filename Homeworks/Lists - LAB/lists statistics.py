number = int(input())
positive = []
negative = []

for _ in range(number):
    n = int(input())
    if n < 1:
        negative.append(n)
    else:
        positive.append(n)
        
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")