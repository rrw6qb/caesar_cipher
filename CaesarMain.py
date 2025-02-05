import CaesarInputPrompter as cip 
import CaesarEncoder as ce
import CaesarDecoder as cd
import sys
global shiftNumber

def main():
    user_response = input("Welcome to Caesar-Cipher! If you would like to encode type 'encode' if you would like to decode type 'decode'")
    user_response = user_response.lower()
    if user_response == "encode":
        phrase = cip.phrase_obtainer()
        shiftnumber = cip.cc_shift_number()
        encoded_phrase = ce.encoder(phrase,shiftnumber)
        print("Encoded Phrase: ", encoded_phrase)
    if user_response == "decode":
        pass
    else:
        print("Incorrect input, Goodbye!")
        sys.exit
        
        
if __name__ == '__main__':
    main()