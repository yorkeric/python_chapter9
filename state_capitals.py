def get_state_capitals_dictionary():
    # Open file containing state capitals for read
    state_capitals_file = open("state_capitals.txt", "r")
    # Loop file and for each line split on the "," and add the key/value pair to the dictionary
    state_capitals_dictionary = dict(line.strip().split(",") for line in state_capitals_file)
    # Close the file
    state_capitals_file.close()
    return state_capitals_dictionary