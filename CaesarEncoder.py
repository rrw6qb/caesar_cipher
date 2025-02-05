
def encoder(phrase, shiftNumber):
    words = phrase.split()
    updated_words =[]
   
    for word in words:
        concat_word = ""
        for c in word:
            updated_c = ord(c) + shiftNumber
            concat_word += chr(updated_c)
        updated_words.append(concat_word)
    encoded_words= " ".join(updated_words)
    return encoded_words


        

         
