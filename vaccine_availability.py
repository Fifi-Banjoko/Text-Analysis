"""
PROBLEM: Vaccine Availability by County

Points: 50 
Extra Credit (Maximum Possible 25 Points): 
    Option 1: 5 points
    Option 2: 5 points for line plot/pie chart, 2 points for colored bar chart
    Option 3: 8 points
    Option 4: Variable, up to 15 points depending on solution

This problem exercises your knowledge of working with strings and dictionaries, as well as reading in and processing a real-world CSV file (in Python).

You are supposed to read in the CSV file provided, process it to get the vaccine availability for each county and then make a bar chart for the top 20 counties having the largest number of vaccines available.

Sample output for the dictionary output for top 20 counties has been shown in 'vaccine_availability.txt' and sample output for the bar chart has been shown in 'vaccineprovideraccessibilitydata_output.png'  

Data source: https://www.dshs.texas.gov/coronavirus/additionaldata/
* "COVID-19 Vaccine Provider Dashboard: This dashboard contains data on vaccine providers in Texas. The Texas Vaccine Provider Data (.csv) contains the underlying data currently displayed on the main dashboard."

Extra credit:
* Option 1: For CSV files with quotes containing commas (e.g., "Austin, TX"), handle them correctly; here we simply ignore any line containing " to simplify processing

* Option 2: Only a bar chart is required; you could also make a line plot and/or pie chart as we've covered in class.  A colored bar chart (random colors for different bars) is not required but can be done for modest extra credit.

* Option 3: While we are making a bar chart for the top 20 counties, there can be a feature to make it for any number of counties that we want. Modify the def get_top_counties function to have an addtional argument for the top number of counties we desire. This argument can be given while running the program, like so:
TOP=10
top_counties = get_top_counties(vaccine_count, TOP)

* Option 4: Real-world CSV data is noisy -- we simply throw out lines that fail a couple of simple checks, but you could do more robust processing.  If so, you'll need to document what you did and why to better handle the noisy data. One example can be that the numbers for vaccine availability can be entered withing parantheses (Instead of having '500' the file had '(500)'). 
"""
# suppress matplotlib warning in replit
import os
import tempfile
os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()

# library for plotting figures
import matplotlib.pyplot as plt
import random # bar chart colors

import word_count  # re-use functions

"""
Read in from the file a list of sentences, one sentence per line, and return this list.
"""
def read_lines(filename):
    return word_count.read_lines(filename)

"""
Return the most frequent word in the dictionary
"""
def get_top_word(word_dict):
    return word_count.get_top_word(word_dict)

"""
Given a parameter line containing comma-separated values (CSV data), process it to extract the name of the county and integer count of vaccines available in that county.  Note, some lines cannot be processed, in which case we indicate that the line could not be processed by returning None for the count (and anything for the county). The pseudocode algorithm is below.

If you look at the raw CSV file, you will see each line corresponds to a vaccine provider in TX, hence there are multiple vacine providers from the same county on different lines of the file.

If the line does not contain a quote character (")
    Split the line into a list of strings
    If the county (at list index INDEX_COUNTY) is not an empty string
        If the vaccine count (at list index INDEX_COUNT) can be converted to an integer without raising an exception
            return county, count
Otherwise return None for the count (and anything for county)

Rationale:
* CSV files use quotes to enclose fields that contain internal commas (e.g., "Austin, TX" is intended to be one field in the data and not split). This complicates data processing, so we will simply ignore these lines
* Real-world CSV data is noisy.  In this case, many counties are empty strings, or vaccine count values are not integer, hence we ignore those lines as well
"""
def parse_line(line):
    INDEX_COUNTY = 5
    INDEX_COUNT = 15
    county = None
    count = None
    if '"' not in line:
        strings = line.split(' ')
        county = strings[INDEX_COUNTY]
        if county and len(strings) > INDEX_COUNT:
            count = (strings[INDEX_COUNT])
    return county, count

"""
Given a parameter list of lines read from the CSV file, process each line one by one, extracting the county and vaccine availability at that county from the line.  Lines which cannot be processed should be ignored (i.e., excluded from the dictionary).  Create a dictionary in which each county is a key and the value is the total count of vaccines availability in that county.  Return the dictionary created.

Start by deleting the first line from the list (header row in CSV file)

Extra credit: because the raw text in the CSV file is noisy, the same county might be erroneously capitalized in different ways (e.g., Travis, tRAvis, TraVIS, etc.). If this is not corrected, then each capitalization variant will be a different entry in the dictionary. For extra credit, fix each county to be properly capitalized before adding it to the dictionary.
"""
def create_dictionary(lines):
    vaccine_count = {}
    lines = lines[1:]
    for line in lines:
        county, count = parse_line(line)
        if count:
            county = county.lower()
            if county in vaccine_count:
                vaccine_count[county] += count
            else:
                vaccine_count[county] = count

    return vaccine_count

"""
Given the parameter a dictionary of vaccine counts by county create a new dictionary that only contains the top 20 counties that have the largest availability of vaccines.

Import word_count at the top of this file and use its word_count.get_top_word() function to find the county with the highest vaccine availability and that availability count.
"""
def get_top_counties(vaccine_count, NUM_counties):
    top_counties = {}
    NUM_COUNTIES = 20
    while NUM_COUNTIES > 0:
        NUM_COUNTIES-=1
        county = word_count.get_top_word(vaccine_count)
        count = vaccine_count[county]
        vaccine_count.pop(county)
        top_counties[county] = count
    return top_counties

# #Extra credit
# def get_top_counties(vaccine_count, TOP):
#     TOP = int(input('Top desired counties\n'))
#     while TOP > 0:
#         TOP -= 1
#         county = word_count.get_top_word(vaccine_count)
#         count = vaccine_count[county]
#         vaccine_count.pop(county)
#         top_counties[county] = count
#     return top_counties

"""
Given a dictionary of counties with the most vaccine availability, display the number of counties in the dictionary and then each of the counties and its availability count.
"""
def display_top_counties(top_counties):
    print(f'Top {len(top_counties)} counties by vaccine availability:')
    for county, count in top_counties.items():
        print(f'{county}: {count}')

"""
Given parameters for 1) a dictionary of counties with the most vaccine availability, 
and 2) and output image filename for the barchart, save a bar chart of the counties (labels) 
and their vaccine availability count (bar height).

Note: if your axis labels are clipped, try using
        plt.tight_layout()
before saving the plot image

Note 2: if you your x-axis labels are cluttered, try rotating them
        plt.xticks(centers, labels, rotation=45) 
where rotation is in degrees, e.g., 45 degrees here, or 90, etc.
"""
def create_bar_chart(top_counties, filename):
    counties = list(top_counties.keys())
    vaccine_availability = list(top_counties.values())

    COLORS = ('b', 'g', 'r', 'c', 'm', 'y', 'k')  # omit 'w' - background color
    num_bars = len(vaccine_availability)
    colors = random.sample(COLORS, k= num_bars)

    #Bar Graph
    fig, ax = plt.subplots(figsize=(10, 10))  # setting the figure size
    plt.bar(counties, vaccine_availability, color= colors)
    plt.title('Vaccine Availability by County')
    plt.xlabel('County')
    plt.ylabel('Vaccine Availability Count')
    # plt.tight_layout()
    plt.show
    plt.savefig(filename+'.png')

    #Line Plot
    plt.plot(counties, vaccine_availability)

    #Pie Chart
    # Pie Chart
    plt.pie(vaccine_availability, labels=counties, labeldistance= None, autopct='%1.0f%%', colors=colors)
    plt.legend(bbox_to_anchor=(1.3, 0.35), loc="lower right")
    plt.title('Vaccine Availability by County')
    plt.show()

"""
Read in a list of lines in the file
Create a dictionary of (county, total vaccine availbility) from the input lines
Create a smaller dictionary of the TOP counties by vaccine availability (if not sure, just take the Top 10)
Display (console text output) the reduced dictionary of top counties
Create a bar chart of top counties with vaccine availability. (Name the image file to be the same as the CSV file, only using a .png filename suffix instead.)
"""
def main():
    print('\nProblem: Vaccine Availability by County\n')

    FILENAME = 'vaccineprovideraccessibilitydata.csv'
    lines = read_lines(FILENAME)

    vaccine_count = create_dictionary(lines)
     
    NUM_COUNTIES=20
    top_counties = get_top_counties(vaccine_count, NUM_COUNTIES)

    display_top_counties(top_counties)

    # Name the image file to be the same as the CSV file, only using a .png filename suffix instead.
    plot_filename = FILENAME.replace('csv', 'png')
    create_bar_chart(top_counties, plot_filename)