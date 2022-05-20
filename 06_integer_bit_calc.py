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






# Converts decimal to binary and states how many 
# bits are needed to represent the original integer
def int_bits():

    #get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0 )






















