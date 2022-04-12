
# functions go here

# puts a series of symbols at the start and end of the text
def statement_generator(text, decoration):

    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# main routine goes here
statement_generator("hello world", "-")






























