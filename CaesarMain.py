import CaesarInputPrompter as cip 
import CaesarEncoder as ce
global shiftNumber

def main():
    print("Welcome to Caesar-Cipher!")
    phrase = cip.phrase_obtainer()
    shiftnumber = cip.cc_shift_number()
    ce.encoder(phrase,shiftnumber)
    
      
if __name__ == '__main__':
    main()