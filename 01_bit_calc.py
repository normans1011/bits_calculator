
# Functions go here

# Puts a series of symbols at the start and end of the text
def statement_generator(text, decoration):

    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    

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
        print()
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


# Checks if input is a number more than a given value
def num_check (question, low):

    valid = False
    while not valid:

        error = "please enter an integer that is more than or equal to {}".format(low)
        error_2 = "please enter an integer"
        try:
            
            # ask user to enter a number
            response = int(input(question))
            
            
            # checks number is more than zero
            if response >=low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error_2)
            print()

# Calculates the number of bits for a text (# of characters x 8)
def text_bits():

    print()
    # ask user for a string...
    var_text = input("Enter some text: ")
    
    # calculate # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working
    print()
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    print("# of bits is {} x 8 ...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""

# Finds number of bits for 24 bit colour
def image_bits():

    print()
    # ask user for a string...
    height = num_check("Image height: ", 1)
    width = num_check("Image width: ", 1)

    # calculate # of bits (length of string x 8)
    pixels = width * height
    num_bits = pixels * 24

    # output answer with working
    print()
    print("image has {} pixels ...".format(pixels))
    print("# of bits is {} x 24 ...".format(pixels))
    print("We need {} bits to represent the image".format(num_bits))
    print()

    return ""

# converts decimal to binary and states how many bits are
# needed to represent the original integer
def int_bits():

    #get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0 )


    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_binary)

    # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print(" # of bits is {}".format(num_bits))
    print()

    return ""

# Main routine goes here


# Heading
statement_generator("hello world", "-")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going=="":

    # Ask the user for the file type
    data_type = user_choice()
    print()
    print ("You chose", data_type)

    # For integers, ask for integer
    if data_type == "integer":
        int_bits()


    # For images ask width and height
    # (must be an integer more than / equal to 0)
    elif data_type == "image":
        image_bits()
      
    # for text, ask for a string
    else:
        text_bits()


    print()
    keep_going = input(" Press <enter> to continue or any key to quit: ")
    print()
    



























