#checks user choice is 'integer', 'text', or 'image'
def user_choice():

    valid = False 
    while not valid:

        # ask user for choice and change respsonse to lowercase
        response =  input("File type (integer / text / image): ").lower()

        if response == "text" or response == "t":
            return "text"

        else:
            print("Please choose a valid file type!")
            print()

#main routine goes here
data_type = user_choice()
print ("You chose", data_type)

























