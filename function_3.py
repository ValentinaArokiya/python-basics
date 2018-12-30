# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# # # animal_crackers('Levelheaded Llama') --> True
# # # animal_crackers('Crazy Kangaroo') --> False


def two_word(text):
    wordlist = text.lower().split()  # convert both words to lower/upper case to do the comparison.
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]

result = two_word("awesome Apples")
print(result)

