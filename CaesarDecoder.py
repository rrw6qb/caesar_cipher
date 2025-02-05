def decoder(phrase,shiftNumber):
    words = phrase.split()
    original_words =[]
   
    for word in words:
        concat_word = ""
        for c in word:
            updated_c = ord(c) - shiftNumber
            concat_word += chr(updated_c)
        original_words.append(concat_word)
    decoded_words= " ".join(original_words)
    return decoded_words