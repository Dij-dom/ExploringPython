Mountains= {'Makalu': {'height': 8485, 'range': 'himalaya'},
        'Lhotse': {'height': 8516, 'range': 'himalaya'},
        'Mt. Everest': {'height': 8888, 'range': 'himalaya'},
        'K2': {'height': 5611, 'range': 'himalaya'}}
# For the given dictionary d find the solution for the following questions:

#1.Find the mountain with the highest elevation value.
highest_mountain = None
highest_height = 0

for mountain, key in Mountains.items():
    height = key['height']
    if height > highest_height:
        highest_height = height
        highest_mountain = mountain

print(f"The highest mountain peak is {highest_mountain} with ({highest_height} meters)")

#2. Identify the distinct ranges

distinct_ranges = set(mountain['range'] for mountain in Mountains.values())
print("\nMountain ranges are", distinct_ranges)

#3. Sort the dictionary in descending order of the keys
sorted_mountains = dict(sorted(Mountains.items(), reverse=True))
print("\nMountains sorted in descending order of keys:")
for mountain, details in sorted_mountains.items():
    print(f"{mountain}: {details}")

#4. Add two more mountains to the existing dictionary
for i in range(2):
    mountain_name = input("Enter the name of the new mountain: ")
    mountain_height = int(input("Enter the height of the new mountain (in meters): "))
    mountain_range = input("Enter the range of the new mountain: ")

    Mountains[mountain_name] = {'height': mountain_height, 'range': mountain_range}
print("\nNew Mountains dictionary:")
for mountain, details in Mountains.items():
    print(f"{mountain}: {details}")