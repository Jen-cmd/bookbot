def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_tuples = get_character_count(text)
    sorted_tuples = sorted(char_tuples, key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_tuples)
    report = f"--- Begin report of books/frankenstein.txt ---\n\n{num_words} words found in the document\n"
    end = "\n\n--- End report ---"
    
    for key in sorted_dict:
        if key.isalpha():
            report += f"\nThe '{key}' was found {sorted_dict[key]} times"
    
    print(report + end)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = text.lower()
    character_counts = {}
    for char in characters:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts.items()

main()