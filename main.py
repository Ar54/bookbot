from stats import filter_messages 
from stats import count_characters
from stats import listOfDict
from stats import sorted_list
import sys
 


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def main():
        if len(sys.argv) != 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
        file_path = sys.argv[1]
        book_text = get_book_text(file_path)
        character_count = count_characters(book_text)
        convert_dict = listOfDict(character_count)
        print(f"Found {filter_messages(book_text)} total words")
        print(character_count)
        convert_dict.sort(key=sorted_list, reverse=True)
        for entry in convert_dict:
                if entry["char"].isalpha():
                        print(f"{entry['char']}: {entry['num']}")

main()         


    
    

    
    



