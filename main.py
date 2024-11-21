def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_words(text)
    print(f"{num_words} words were found in the text")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_words(text):
    words = text.split()
    return len(words)


if __name__ == "__main__":
    main()