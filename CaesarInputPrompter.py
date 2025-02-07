import sys




def phrase_obtainer():
    u_r = input("Please type what you would like to be encoded/decoded: ")
    return u_r
    


def cc_shift_number():

    global shiftNumber

    try:
        shiftNumber= int(input("Provide a shift number, using '-' to denote a reverse shift. ENSURE the number is between -26 and 26\n"))
    except ValueError:
        print("A character that is not a number was entered. Please try again.")
        cc_shift_number()

    if -26 <= shiftNumber <= 26:
        return shiftNumber
        
    while (not -26 <= shiftNumber <= 26):
        try:
            shiftNumber= int(input("Either you did not type a number or you number does not meet the constraints outlined. Please try again\n"))
        except ValueError:
            print("A character that is not a number was entered. Goodbye")
            sys.exit()
    return shiftNumber


