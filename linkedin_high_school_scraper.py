import pandas as pd
from bs4 import BeautifulSoup
import re

HIGH_SCHOOL_KEYWORDS = [
    'High School', 'Academy', 'Institute', 'College', 'Secondary School', 'Prep School',
    'Senior High School', 'Junior High School', 'Vocational School', 'Trade School', 'High School Diploma'
]

def extract_high_school_from_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            
            education_section = soup.find('section', {'id': 'education-section'}) or soup.find('div', {'class': 'education-section'})
            
            if education_section:
                text_elements = education_section.find_all(text=True)
                
                for text in text_elements:
                    for keyword in HIGH_SCHOOL_KEYWORDS:
                        if keyword.lower() in text.lower():
                            possible_high_school_names = re.findall(r'\b[\w\s\'-]+(?:{}|{})\b'.format(
                                '|'.join(re.escape(keyword) for keyword in HIGH_SCHOOL_KEYWORDS), keyword
                            ), text, re.IGNORECASE)
                            if possible_high_school_names:
                                return possible_high_school_names[0].strip()
                
            return 'High School not found'
    except Exception as e:
        return f'Error processing file: {e}'

def main():
    input_file = 'input_linkedin_profiles.csv'
    output_file = 'output_high_schools.csv'
    
    df = pd.read_csv(input_file)
    high_schools = []
    
    for index, row in df.iterrows():
        file_path = row['url'].replace('file:///', '')
        high_school = extract_high_school_from_html(file_path)
        high_schools.append(high_school)
    
    df['High School'] = high_schools
    df.index = df.index + 1
    df.to_csv(output_file, index_label='Index')
    print(f"Extraction completed. Results saved to {output_file}")

main()
