# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
import re

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]
#function that finds how many instances the word appears in the email and censors it.
def censor_string(word, string):
    censored_string = string.replace(word, ("X"*len(word)))
    censored_string = string.replace(word.title(), ("X"*len(word)))
    censored_string = string.replace(word.upper(), ("X"*len(word)))
    return censored_string

#uncomment to test censor_string fucntion
#test = censor_string("learning algorithms", email_one)
#print(test)

# function finds all instances proprietary terms appear in the email and censors it.
def censor_string_from_list(list, string):
    list = sorted(list, key=len)
    list.reverse()
    for str in list:
        string = string.replace((" " + str), (" " + "X" * len(str)))
        string = string.replace((" " + str.title()), (" " + "X" * len(str)))
        string = string.replace((" " + str.upper()), (" " + "X" * len(str)))
    return string

#uncomment to test censor_string_from_lsit fucntion
#print(censor_string_from_list(proprietary_terms, email_two))

#function finds proprietary terms and negative words that occur more than twice
def negative_words_occurance(list, string):
    list = sorted(list, key=len)
    list.reverse()
    string = censor_string_from_list(proprietary_terms, string)
    index_list = []
    new_string = ""
    new_string_negatives = ""
    for str in list:
        for m in re.finditer(str, string):
            index_list.append(m.end())
    index_list.sort()
    second_negative = index_list[1]
    new_string = string[:second_negative]
    new_string_negatives = string[second_negative:]
    if len(index_list) > 2:
        for str in list:
            new_string_negatives = new_string_negatives.replace((" " + str), (" " + "X" * len(str)))
            new_string_negatives = new_string_negatives.replace((" " + str.title()), (" " + "X" * len(str)))
            new_string_negatives = new_string_negatives.replace((" " + str.upper()), (" " + "X" * len(str)))
        return new_string + new_string_negatives
    else:
        return string


#uncomment to test negative_words_occurance
#print(negative_words_occurance(negative_words, email_three))
