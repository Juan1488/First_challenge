# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
#function that finds how many instances the word appears in the email
def censor_string(word, string):
    word_count = string.count(word)
    return f"\"{word}\" was found {word_count} times in this email"

#uncomment to test censor_string fucntion
#test = censor_string("learning algorithms", email_one)
#print(test)

# function finds all instances proprietary terms appear in the email
def censor_string_from_list(list, string):
    word_count_complete = ""
    for str in list:
        word_count = string.count(str)
        word_count_complete += f"\"{str}\" was found {word_count} time(s) in this email.\n"
    return word_count_complete

#uncomment to test censor_string_from_lsit fucntion
#print(censor_string_from_list(proprietary_terms, email_two))

#function finds proprietary terms and negative words that occur more than twice
def negative_words_occurance(list, string):
    proprietary_terms_occurance = censor_string_from_list(proprietary_terms, string)
    neggative_more_than_twice = ""
    word_count = 0
    for str in list:
        word_count += string.count(str)
    if word_count > 2:
        neggative_more_than_twice += f"\nNegative words are present more than twice in this email. there are {word_count} negative words in this email.\n"


    return proprietary_terms_occurance + neggative_more_than_twice

#uncomment to test negative_words_occurance
#print(negative_words_occurance(negative_words, email_three))
