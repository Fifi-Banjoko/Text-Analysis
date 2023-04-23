"""
PROBLEM: Image Search Using Tags

Points: 50
Extra Credit: see below

This problem exercises your knowledge of working with sets and dealing with csv files, and generally provides training and assessment for data science.

One way to perform image search is to match keywords in a user's textual search query to "tags" describing what is in an image. For example, see
* https://www.canto.com/blog/image-tagging/
* example image and tags: https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/01/image-tagging-2.jpg

The csv file 'search_images.csv' contains the URLs for different Flickr images, their IDs, and up to six tags that describe each image.
Your program will ask the user to enter a search query of keywords, then display the ID and tags of all images whose tags match those keywords.

The file 'search_images_output.txt' has an example of expected program output.

EXTRA CREDIT: instead of finding and displaying a set of image search results, create and display search results as a ranking.
Create a modified copy of the input CSV file in which tags have associated weights (e.g., flora:0.5), where weights indicate that some tags are more salient to the image than others.
Then when you perform matching against query keywords, calculate the weight of each match (the sum of weights of matching terms), and display matching images in rank order from highest to lowest weight of match, including the weight of each match.  Google does something like this internally when it gives you a ranked list of image search results! For an example of weighted tags, see image from blog post above: https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/01/image-tagging-3.jpg.

MORE INFORMATION:
* This data is sourced from the British Library (https://www.flickr.com/photos/britishlibrary/). 

* Explore a GoogleSheet of URLs to images and their tags https://docs.google.com/spreadsheets/d/1mupWcEsU6py4gAvemUBjRzcgw4RLlBDoHwlPViwjkvo/edit?usp=sharing. 

* Our dataset is derived from https://figshare.com/articles/dataset/BL_Flickr_image_dataset_User_Submitted_Tags_til_March_2016_/3126481
"""
import search_text  

"""
Read in a list of lines from the input file and return this list.
"""
def read_lines(filename):
    return search_text.read_lines(filename)


"""
Each line contains comma-separated values (CSV data), from which we want to extract the URL, ID and set of image tags. You can assume each image has at least one tag.

Delete/skip the first line (header row in CSV file)
For each line
    Split the line into a list of strings
    Create a key for each image from the URL and ID: "Image ID: URL" 
        (See program output example for key that will be printed)
    Create a set of the image tags
    Add the image to the dictionary, mapping its key to its tag set
return the dicitonary
"""
def create_dictionary(lines):
    image_dict = {}
    lines = lines[1:] #skipping the first line and starting at index 1
    for line in lines: #loop through lines
        strings = line.split(',') #split the line into a list of strings
        key = f'{strings[1]}: {strings[0]}' #"Image ID: URL"
        tags = set(strings[2:])
        image_dict[key] = tags

    return image_dict


"""
Prompt the user for their search query (tags to match) and return the set of tags.
"""
def get_user_query():
    query_tags = set(input('Enter query tags separated by commas\n').split(','))
    return query_tags


"""
Search for images whose tags that match the query. There is a match if (and only if) all of the query tags are found in the image's tag set.

Example: 
* if the user query set is 'cat','black'
* then for an image with tags 'cat','black','small' return True
* but for an image with tags 'cat','white','furry' return False
HINT: are the query tags a subset of the image tags?

For each image in the dictionary
    if it matches, display its key
Display the total number of matches found.

See example of program output for further guidance on display format.
"""
def display_matches(query_tags, image_dict):
    print('Results:')
    count = 0
    for key, tags in image_dict.items(): #loop through key and tags of image_dict
        if query_tags.issubset(tags): #if all the query_tags are in the image dict tag print the key of the tag
            print(key)
            count+=1 #add one to the count of the matches
    # fix!
    print(f'{count} matches found.')


"""
Read in a list of lines from the input file 
Create a dictionary mapping each image ID & URL to its set of descriptive tags
Loop
    Prompt the user for their search query (i.e., image tags to match)
    Find and display any matching images (using the dictionary)
    Prompt the user to ask if they want to search again; end the loop if not
        Allow any capitalization of "yes" to continue (e.g., YES, yes, YeS, etc.)
Print "Goodbye!" before the program terminates.
"""
def main():
    print('\nProblem: Image Search using Tags\n')
    FILENAME = 'search_images.csv'

    # fill in
    lines = read_lines(FILENAME)
    dictionary = create_dictionary(lines)
    dosearch = 'yes'
    while dosearch == 'yes':
        query_tags = get_user_query()
        display_matches(query_tags, dictionary)
        dosearch = input('Do you want to search again??(Yes/No) >>>> ').lower()

    print('\nGoodbye!')

