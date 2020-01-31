words = input("Enter the sentence: ").split()

counts = []

for i in range(len(words)):
    counts.append(0)

for i in range(len(words)):
    for j in range(len(words)):
        if words[i] == words[j]:
            counts[i] += 1

print("Word\tCount")

for i in range(len(words)):
    print(words[i], "\t", counts[i])
