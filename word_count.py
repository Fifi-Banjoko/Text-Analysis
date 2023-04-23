"""
PROBLEM: Word Count

Points: 50
Extra Credit (Maximum Possible 10 Points): 
    Option 1: 3 Points
    Option 2: 7 Points

This problem exercises your knowledge of working with dictionaries (in Python).

Conversational assistants like Alexa and Siri use automatic speech recognition (ASR) to transcribe what people say into text.
Often this is difficult because many things people say sound the same, such as “a”, “the”, or “uh”.
Consequently, a trick to improve ASR accuracy is make a list of which words are most frequent; when the program isn’t certain whether the user said “a”, “the”, or “uh”,
it will then assume the more frequent word was said. To enable this, we must count how often each word occurs.

In this problem, you will implement this using the 'text.txt' file. After processing the file, you are supposed to generate a dictionary contatining the words and their word counts.
See 'word_count_output.txt' for sample output, including outputs for extra credit options.

The first thing that is typically required in most text analysis is preprocessing: changing text to lowercase, removing punctuation, and breaking hyphenated tokens into separate words.  So we have to do this before we can count words.

See main() for pseudocode to implement.

Extra Credit:
* Option 1: Estimate the probability of each word as its count divided by the total count of all words. Display the 10 most probable words and their probabilities (displayed to 4 digits of precision), sorted by decreasing probability.

* Option 2: Create a second dictionary that maps from each letter in the alphabet to the most probable word starting with that letter.  Prompt the user for a word and then output the most probable word which starts with the same letter as the input word. Why?  Have you noticed as you are typing that a program sometimes suggest the rest of the word, given only the first letter you've typed?  This is how they do it!
"""
import preprocess

"""
Read in a list of lines from the input file and return this list.
"""
def read_lines(filename):
    return preprocess.read_lines(filename)

"""
Given a list of lines, modify each line by: 
* converting it to lowercase
* replacing all hyphens ('-') by spaces (' ')
* keeping only alphanumeric characters and whitespace
"""
def preprocess_lines(lines):
    preprocess.preprocess_lines(lines)

"""
Create a dictionary of unique words that occur in the document. Each unique word should be a key in the dictionary, 
with an associated dictionary value: the total number of times that word occurs in the document.
"""
def create_dictionary(sentences):
    '''
    Split each sentence to words, if word is in word dict, increase the count of word
    If not add word to word dict and set count as 1
    '''
    word_dict = {}
    for sentence in sentences:
        words = sentence.split(' ')
        for word in words:
            if word in word_dict:
                word_dict[word]+=1
            else:
                word_dict[word]=1    
    return word_dict

"""
Return the most frequent word in the dictionary
"""
def get_top_word(word_dict):
    top_word = None
    '''There's a bit of trickery going on below, but trust me it's simple
    So, the word dict has the words in the key and the frequency in the values right?
    Something like this {'of':5, 'and':3, 'to':2, 'a':6 ...}
    To get the most frequent, from right to left in the function,
    we first get all the values in the dictionary as a list, 
    then we get the max of that list
    then we search for the index of that max from a list of the values
    then we get the word from a list of the keys at the position of the index           
    '''
    top_word = list(word_dict.keys())[list(word_dict.values()).index(max(list(word_dict.values())))]
    return top_word
    
"""
Given a parameter word dictionary with word frequencies, display the 10 most frequent words and the frequency of each

Do COUNT times
   Find the most frequent word and its frequency
   Display the frequency and the word
   Remove the word from the dictionary 
"""
def display_top_words(word_dict):
    COUNT = 10
    print(f'The {COUNT} most frequent words are:')
    while COUNT > 0: #loop through while count is greater than 0
        COUNT-=1 # decrement count so the most frequesnt 10 words are gotten from 10 to 1
        most_frequent_word = get_top_word(word_dict) #use the get_top_word function to get the most frequesnt word and save it as the variable most_frequent_word
        frequency = word_dict[most_frequent_word] #get the value of the most_frequent_word key from the dictionary, which is the frequency of that word
        word_dict.pop(most_frequent_word) #remove the word from the dictionary
        print(f'{frequency} : {most_frequent_word}') #print the word and the frequency (number of times it occurs in the dictionary)


"""
Read in a list of lines from the input document
Process the lines
Create a dictionary of all words and their frequencies in the document
Find and display the top-10 most frequent words and their frequencies
"""
def main():
    print('\nProblem: Word Count\n')
    FILENAME = 'text.txt'   
    lines = read_lines(FILENAME)
    preprocess_lines(lines)
    word_dict = create_dictionary(lines)
    display_top_words(word_dict)
