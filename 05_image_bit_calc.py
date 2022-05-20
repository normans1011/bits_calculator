

def num_check (question, low):

    valid = False
    while not valid:

        error = "Please enter a number that is more than (or equal to {}".format(low)
        
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
            print(error)









# calculates the # of bits for the image (height x width x 24)
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


# Main routine goes here
image_bits()




























