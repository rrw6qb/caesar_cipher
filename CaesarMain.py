import CaesarInputPrompter as cip 
import CaesarEncoder as ce
import CaesarDecoder as cd
import sys
global shiftNumber

def main():
    user_response = input("Welcome to Caesar-Cipher! If you would like to encode type 'encode' if you would like to decode type 'decode'\n")
    user_response = user_response.lower()
    
    if user_response == "encode":
        phrase = cip.phrase_obtainer()
        shiftnumber = cip.cc_shift_number()
        encoded_phrase = ce.encoder(phrase,shiftnumber)
        print("Encoded Phrase: ", encoded_phrase)
        raise SystemExit
    if user_response == "decode":
        phrase = cip.phrase_obtainer()
        shiftnumber = cip.cc_shift_number()
        decoded_phrase = cd.decoder(phrase,shiftnumber)
        print("Decoded Phrase: ", decoded_phrase)
        raise SystemExit
    print("Incorrect input, Goodbye!")
    raise SystemExit
        
        
if __name__ == '__main__':
    main()