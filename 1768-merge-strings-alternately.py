def mergeAlternately(word1: str, word2: str) -> str:
    longer = word1 if len(word1) > len(word2) else word2
    shorter = word1 if len(word1) < len(word2) else word2
    word = ""

    for i in range(len(longer)):
        if (i < len(shorter)):
            word += word1[i]
            word += word2[i]
        else:
            word += longer[i]

    return word

def mergeAlternately2(word1: str, word2: str) -> str:
    word = []

    for a, b in zip(word1, word2):
        word.append(a + b)

    word.append(word1[len(word2):])
    word.append(word2[len(word1):])
    
    return "".join(word)

def main():
    print(mergeAlternately("abc", "pqr"))
    print(mergeAlternately2("abc", "pqr"))

main()
