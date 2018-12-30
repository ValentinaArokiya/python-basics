# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(st):
    wordlist = st.split()
    print(wordlist)
    reverse_wordlist = wordlist[::-1]
    print(reverse_wordlist)
    return ' '.join(reverse_wordlist)

print(master_yoda("I am home"))

#### .join() to convert list to string



