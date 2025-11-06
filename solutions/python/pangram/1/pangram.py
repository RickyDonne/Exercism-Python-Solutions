def is_pangram(sentence):
    sentence = sentence.lower()
    sentence = [*sentence]
    alphabets = {}
    for ch in sentence:
        value = alphabets.get(ch)
        if (value is None or value < 1) and ch.isalpha():
            alphabets[ch] = 1

    return (len(alphabets) == 26)
