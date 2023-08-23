import re

def find_matching_indices(pattern, text):
    matches = re.finditer(pattern, text)
    print(matches)
    indices = [match.start() for match in matches]
    return indices

# Example usage
search_pattern = r'\d+'  # a raw string literal in Python used for regular expressions to ensure that backslashes are treated as literal characters and not as escape characters.
text = 'There are 123 apples and 456 oranges, but only 789 bananas.'

matching_indices = find_matching_indices(search_pattern, text)
print("Matching indices:", matching_indices)
