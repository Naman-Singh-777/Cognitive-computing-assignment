import random

print("Solution 1: List Operations")
L = [10, 20, 30, 40, 50, 60, 70, 80]
L.extend([200, 300])
print(L)

L.remove(10)
L.remove(30)
print(L)

L.sort()
print(L)

L.sort(reverse=True)
print(L)

print("\nSolution 2: Tuple Operations")
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

max_score = max(scores)
max_index = scores.index(max_score)
print(f"Highest score: {max_score} at index {max_index}")

min_score = min(scores)
min_count = scores.count(min_score)
print(f"Lowest score: {min_score} appears {min_count} times")

reversed_list = list(reversed(scores))
print(reversed_list)

score_to_find = 76
if score_to_find in scores:
    print(f"Score {score_to_find} found at index {scores.index(score_to_find)}")
else:
    print(f"Score {score_to_find} not found")

print("\nSolution 3: Random Numbers Analysis")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [random.randint(100, 900) for _ in range(100)]

odd_numbers = [n for n in numbers if n % 2 != 0]
even_numbers = [n for n in numbers if n % 2 == 0]
prime_numbers = [n for n in numbers if is_prime(n)]

print(f"Odd numbers: {len(odd_numbers)}")
print(f"Even numbers: {len(even_numbers)}")
print(f"Prime numbers: {len(prime_numbers)}")

print("\nSolution 4: Set Operations")
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

unique_scores = A.union(B)
print(f"Unique scores: {unique_scores}")

common_scores = A.intersection(B)
print(f"Common scores: {common_scores}")

exclusive_scores = A.symmetric_difference(B)
print(f"Exclusive scores: {exclusive_scores}")

is_subset = A.issubset(B)
is_superset = B.issuperset(A)
print(f"A is subset of B: {is_subset}")
print(f"B is superset of A: {is_superset}")

X = int(input("Enter score to remove from A: "))
if X in A:
    A.remove(X)
    print(f"Updated set A: {A}")
else:
    print(f"Score {X} not found in set A")

print("\nSolution 5: Dictionary Key Renaming")
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)
