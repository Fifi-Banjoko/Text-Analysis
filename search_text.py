"""
PROBLEM: Search Text
Points: 50
Extra Credit (Maximum Possible 24 Points): 
    Option 1 - 4 Points
    Option 2 & 3 - 7 Points Each
    Exception Handling & Input Validation - 3 Points Each
    
This problem exercises your knowledge of working with strings (in Python).

Most word processes / text editors allow the user to search a document for a matching word or phrase, to find out where it occurs in the document. We will implement search functionality like this in this problem.

The text file 'text.txt' contains a single sentence in each line. Your program will let the user enter a query (i.e., a word or phrase) and then display all matching lines and line numbers. 

The file 'search_text_output.txt' has sample outputs for you to check your output against

Extra credit options:
* Option 1: Perform case-insensitive search (i.e., ignore case / capitalization in matching).  Matching sentences displayed should retain their original capitalizion. 
* Option 2: Insert the string “ *** ” immediately before and after THE FIRST occurrence of the query string within each matching sentence
* Option 3: Insert the string “ *** ” immediately before and after ALL occurrences of the query string within each matching sentence
* Handle exceptions in file input/output using try/except
* Perform input validation - # Regex- G[a-bA-B].* 
"""

"""
Read in a list of lines from the input file and return this list.
"""
def read_lines(filename):
    lines = None
    with open(filename, mode='r') as f: 
        lines = f.readlines()
    return lines

"""
Search for sentences that contains the query string. Return a list of matching *indices* for the sentence list.  
For example, if there are three sentences and sentence 1 and 3 match, this function should return the list of indices [0,2].
"""
def find_matches(query, sentences):
    matches = []
    for i, sentence in enumerate(sentences): #loop through sentences with a count and value variables
        if query in sentence: #add the indices to the list matches if the query is in the sentence
            matches.append(i)
    return matches

"""
Given two parameters, 1) sentences (a list of strings) and 2) matches (a list of indices into the sentence list), 
display the number of matching sentences, then display each matching line number and the sentence.
"""
def display_matches(sentences, matches):
    print(f'{len(matches)} matching line(s) found:')
    for i in matches: #loop through matches and return the corresponding sentence value for that index
        print(f'{i} {sentences[i]}')
        

"""
Read in sentences from the text file
Loop
    Prompt the user for their search query
    Find the list indices for matching sentences
    Display those sentences and their line numbers
    Prompt the user to ask if they want to search again
        Allow any capitalization of "yes" to continue (e.g., YES, yes, YeS, etc.)
"""
def main():
    print('\nProblem: Search Text \n')
    FILENAME = 'text.txt'   
    sentences = read_lines(FILENAME)
    dosearch = 'yes' #add capitalisation clause
    while dosearch == 'yes': #iterate while dosearch is yes
        try: 
            query = input('Enter search query >>>> ')
            matches = find_matches(query, sentences)
            display_matches(sentences, matches)
            dosearch = input('Do you want to search again??(Yes/No) >>>> ').lower()
        except:
            print('Please enter a valid query')
        
    # Fill in!

    print('Goodbye!')
    