# LinkedIn High School Scraper

This project includes a Python script for extracting high school information from LinkedIn profile HTML files. The script processes local HTML files, searches for high school-related keywords in the education section, and outputs the results to a CSV file.

## Features

- Parses local HTML files representing LinkedIn profiles.
- Extracts high school names based on a predefined list of keywords.
- Outputs results to a CSV file with indexed rows.

## Prerequisites

- Python 3.x
- Required Python libraries: `pandas`, `beautifulsoup4`

## Installation

**Clone the repository:**

   
   git clone https://github.com/f-aiz/linkedin_high_school_scraper.git
   cd linkedin_high_school_scraper

**Install the required Python Libraries**

    pip install pandas beautifulsoup4


## Usage

**Prepare Input CSV File:**

Create a CSV file named input_linkedin_profiles.csv with the following structure:
url
file:///path/to/profile1.html
file:///path/to/profile2.html
...
Replace file:///path/to/profileN.html with the actual paths to your local HTML profile files.

**Run the Script:**

Execute the script using Python:

python linkedin_high_school_scraper.py
This will process the HTML files and generate an output CSV file named output_high_schools.csv.

**Check Output:**

The output CSV file output_high_schools.csv will contain two columns: Index and High School. The Index column represents the row number, and the High School column contains the extracted high school names.

## This project was created by f-aiz.

