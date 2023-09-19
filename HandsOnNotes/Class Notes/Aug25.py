#considering a word file contaning student details and perform the following
# find the number of words lines and paragraphs in the given word document
# find the count of the words starting with capital letters
# identify and find the number of words containing text and number together
# find all the occurences of date in the given document
# replace and by &
# replace " " of first five lines with underscore and 8th line spaces by "-"
# find the occurence and position of the email ids in the choosen document
# identify various groups in the email
# find the text which begins with capital letter and ends with ","
# find the text which begins with the word science
# find all the occurences ending with "ing"
#identify the following patterns.
#   word containing typo errors
#   word containing repeated occurences if the character 3 or more times
#   sentence ending with question mark
#   words where 1 is followed ny 0


import re
with open('ExploringPython\HandsOnNotes\StudentInfo.txt','r') as file:
    content = file.read()
print(content)

#Question1
words = re.findall(r'\b\w+\b', content)
word_count = len(words)

# Count lines
lines = content.split('\n')
line_count = len(lines)

# Count paragraphs (assuming paragraphs are separated by two or more newlines)
paragraphs = re.split(r'\n\s*\n+', content)
paragraph_count = len(paragraphs)

print(f"Total word count is {word_count}\nTotal line count is {line_count}\nTotal paragraphs are {paragraph_count} in number.")

#Question2
capital_words = re.findall(r'\b[A-Z][a-z]*\b', content)
print(f"Total capital words in the text document is {len(capital_words)}")

#Question3
text_and_number_words = re.findall(r'\b\w*\d+\w*\b', content)
num_textwithNum = len(text_and_number_words)
print(f"The number of words containing text and number together is {num_textwithNum}")

#Question4
date_patterns = [
        r'\b\d{1,2}/\d{1,2}/\d{4}\b',     # Matches dates in MM/DD/YYYY format
        r'\b\d{1,2}-\d{1,2}-\d{4}\b',     # Matches dates in MM-DD-YYYY format
        r'\b\d{1,2}\s+\w+\s+\d{4}\b',     # Matches dates in DD Month YYYY format
        r'\b\w+\s+\d{1,2},\s+\d{4}\b'     # Matches dates in Month DD, YYYY format
    ]

all_dates = []
for pattern in date_patterns:
    dates = re.findall(pattern, content)
    all_dates.extend(dates)
count_dates = len(all_dates)
print(f"Number of all the occurences of date in the given document is {count_dates}")

#Question5
modified_text = re.sub(r'\band\b', '&', content)
print(modified_text)

#Question6
lines = content.split('\n')

for i in range(len(lines)):
    if i < 5:
        lines[i] = re.sub(r'\s', '_', lines[i])
    elif i == 7:
        lines[i] = re.sub(r'\s', '-', lines[i])

new_content = '\n'.join(lines)
print(f"The replaced content is given below:\n {new_content}")

#Question7
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
emails = re.findall(email_pattern, content)
print(emails)

#Question8
for email in emails:
    print(f"Email: {email[0]}, Username: {email[1]}, Domain: {email[2]}")

#Question9
pattern = r'[A-Z][a-z]+,'
matches = re.findall(pattern, content)
print(matches)

#Question10
pattern = r'science\w*'
matches = re.findall(pattern, content)
print(matches)

#Question11
result = re.findall(r'\w+ing\b', content)
print(result)

#Question12
result = re.findall(r'\b\w*[aeiou]\w*[aeiou]\w*\b', content)
print(result)

result = re.findall(r'\b\w*(\w)\1{2,}\w*\b', content)
print(result)

repeated_words = re.findall(r'\b(\w*(\w)\2{2,}\w*)\b', content)
print(repeated_words)

question_sentences = re.findall(r'[^.!?]*\?\s*', content)
print(question_sentences)

words_with_10 = re.findall(r'\b\w*10\w*\b', content)
print(words_with_10)





