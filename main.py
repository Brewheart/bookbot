
from stats import get_book_words
import sys



def sort_characters(dict):
    return dict["name"]

def get_character_list(character_count):
    character_list = []
    for i in character_count:
        character_dict = {"name": i, "count": character_count[i]}
        character_list.append(character_dict)

    return character_list


def get_characters(text):
    dict = {}
    string = text.lower()

    for i in string:
        if i in dict:
            dict[i] += 1        
        else:
            dict[i] = 1


    return dict



def get_book_text(path):
    with open(path) as f:
        return f.read()
        

def main():
    if len(sys.argv) < 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_book_words(text)
    character_count = get_characters(text)
    character_list = get_character_list(character_count)


    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    print(character_count)
    character_list.sort(key=sort_characters)

    for i in character_list:
        if i["name"].isalpha():
            print(f"{i['name']}: {i['count']}")


    print ("--- End report ---")


if __name__ == "__main__":
    main()