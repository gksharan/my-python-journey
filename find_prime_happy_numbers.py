# Step 1: Read prime numbers from file
with open("one.txt", "r") as f:
    primes = [int(x) for x in f.read().split()]   # already integers

# Step 2: Read happy numbers from file
with open("others.txt", "r") as f:
    happy = [int(x) for x in f.read().split()]

# Step 3: Find numbers that are both prime and happy
common_numbers = set(primes) & set(happy)   # intersection

# Step 4: Sort and print
for num in sorted(common_numbers):
    print(num)
