
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


def get_book_words(text):
    words = text.split()
    return len(words)



def get_book_text(path):
    with open(path) as f:
        return f.read()
        

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_words(text)
    character_count = get_characters(text)
    character_list = get_character_list(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words were found in the text")

    print(character_count)
    character_list.sort(key=sort_characters)

    for i in character_list:
        if i["name"].isalpha():
            print(f"The '{i['name']}' character was found {i['count']} times")


    print ("--- End report ---")


if __name__ == "__main__":
    main()