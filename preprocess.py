"""
PROBLEM: Preprocess

Points: 50

This problem involves: file input (Ch. 6), list processing (Ch. 7), string processing (Ch.8), and use of sets (Ch. 9).  It both teaches and assesses ability to do text-related data science.

In processing and analysis of textual data in data science, the first thing that is typically required is "normalizing" text via preprocessing: 
* changing text to lowercase
* removing punctuation
* breaking hyphenated tokens into separate words

Furthermore, given a large body of text (known as a "corpus", from latin), we build a "lexicon": a set of all unique words found in the corpus.
This is like an English dictionary but without the definitions (just the words themselves). This is why we use a Python set and not a Python dictionary.

Given an input document that has been preprocessed, we finally:
* replace all numbers (e.g., 157) with a fixed token, such as "NUM"
* replace any document word not found in the lexicon with a fixed token, such as "UNK"

See the pseudocode algorithm for each function below for details of what you need to implement.

Fun Trivia: the corpus file we use here comes from Peter Norvig, the Director of Research at Google! https://norvig.com/big.txt (we've renamed this corpus.txt and slightly shortened it)
"""
import search_text
"""
Read in a list of lines from the input file and return this list.
"""


def read_lines(filename):
    return search_text.read_lines(filename)


"""
Given a list of lines, modify each line by: 
* converting it to lowercase
* replacing all hyphens ('-') by spaces (' ')
* keeping only alphanumeric characters and whitespace
"""


def preprocess_lines(lines):
    for i in range(len(lines)): #loop through the lines but with the position(index)
        line = lines[i] #get the line in the index we are at
        line = line.lower().replace('-', ' ') #convert line to lower, then replace hyphen with space
        newline = '' #holder var initialized as empty string
        for char in line: #loop though each of the characters in the line
            if char == ' ' or char.isalnum(): #if the char is space or is alphanumeric
                newline+=char #add to the holder variable
        lines[i] = newline #replace line at index with new line
    return lines


"""
Given a list of preprocessed lines, return a new lexicon (i.e., a set of all unique words that occur)
"""


def create_lexicon(lines):
    lexicon = set() #create a set called lexicon
    for line in lines: #loop through lines
        words = line.split(' ') #split the line into individual words and add to set
        lexicon.update(set(words))
    return lexicon


"""
Given a list of preprocessed tweets and a lexicon (set) of words, modify the list of tweets as described below.

For each tweet
    For each word in the tweet
        if the word is a non-negative integer, replace it with NUMBER
        If not, check if the word is in the lexicon
            If it is in the lexicon, keep it; otherwise replace it with UNKNOWN
"""


def filter_tweet_words(tweets, lexicon):
    NUMBER = 'NUM'
    UNKNOWN = 'UNK'
    for i, tweet in enumerate(tweets): #loop through tweets
        words = tweet.split(' ') #split tweet into individual words
        for j, word in enumerate(words): #loop through words
            if word.isdigit(): #if the word is a digit replace it with the value of the variable NUMBER
                words[j] = NUMBER
            elif word not in lexicon: #if the word is not in the lexicon replace it with UNKNOWN
                words[j] = UNKNOWN
        tweets[i] = ' '.join(words) #join words with spaces



"""
Read in a list of lines
    from the corpus file
    from the tweets file
Preprocess each list of lines
Create lexicon
Filter tweet words
Display output
"""


def main():
    print('\nProblem: Preprocess\n')
    CORPUS_FILENAME = 'corpus.txt'
    TWEETS_FILENAME = 'tweets.txt'
    corpus = read_lines(CORPUS_FILENAME)
    tweets = read_lines(TWEETS_FILENAME)
    preprocess_lines(corpus)
    preprocess_lines(tweets)

    lexicon = create_lexicon(corpus)
    filter_tweet_words(tweets, lexicon)
    print(tweets)
