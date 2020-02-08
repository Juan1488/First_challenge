# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#function that finds how many instances the word appears in the email
def censor_string(word, string):
    word_count = string.count(word)
    return f"{word} was found {word_count} times in this email"

#uncomment to test censor_string fucntion
#test = censor_string("learning algorithms", email_one)
#print(test)
