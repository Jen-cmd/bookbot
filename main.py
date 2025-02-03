#first_iteration refactored by ChatGPT o1

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    num_words = count_words(text)
    character_counts = count_characters(text)
    sorted_characters = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)
    
    report_lines = [
        f"--- Begin report of {book_path} ---",
        f"{num_words} words found in the document"
    ]
    
    for char, count in sorted_characters:
        if char.isalpha():
            report_lines.append(f"The '{char}' character was found {count} times")
    
    report_lines.append("--- End report ---")
    
    # Print the report
    print("\n".join(report_lines))

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    text_lower = text.lower()
    counts = {}
    for char in text_lower:
        counts[char] = counts.get(char, 0) + 1
    return counts

main()
