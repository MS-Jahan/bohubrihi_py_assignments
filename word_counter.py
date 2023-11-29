search_words = ["Python", "C", "OOP", "Hello", "Java"]

# Open the file
file = open("input.txt", "r", encoding="utf-8")

# Read the file
data = file.read()

# Close the file
file.close()

# Count the words case insensitive
for word in search_words:
    word_count = data.lower().count(word.lower())
    print(f"{word} -> {word_count}")

