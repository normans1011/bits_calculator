
# Functions go here

# Puts a series of symbols at the start and end of the text
def statement_generator(text, decoration):

    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# Checks if user choice is 'integer', 'text', or 'image'
def user_choice():

    #list of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic", "p"]

    valid = False 
    while not valid:

        # ask user for choice and change respsonse to lowercase
        response =  input("File type (integer / text / image): ").lower()

        #checks for valid response and returns text, integer, or image

        if response in text_ok:
            return "text"
        
        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer= input("Press <enter> for an integer or any key for an image: ")
            if want_integer == "":
                return "integer"
            else:
                return "image" 

        else:
            #if response is not valid, output an error
            print("Please choose a valid file type!")
            print()

# Main routine goes here
statement_generator("hello world", "-")

# Heading


# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going=="":

    # Ask the user for the file type
    data_type = user_choice()
    print ("You chose", data_type)

    # For integers, ask for integer
    # (must be an integer more than / equal to 0)


    # For images ask width and height





























