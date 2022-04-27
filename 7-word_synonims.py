n = int(input())
synonyms = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")
