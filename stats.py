
def filter_messages(text):
        words = text.split()
        return len(words)

def count_characters(book_string):
    lower_case = book_string.lower()
    character_dict = {}
    
    for character in lower_case:
        if character in character_dict:
                character_dict[character] +=1
        else:
              character_dict[character] = 1
    return character_dict


def listOfDict(raw_input):
      result = [{"char": key, "num": raw_input[key]} for key in raw_input]
      return result

def sorted_list(input):
      return input["num"]
   

    
      
  
    
        
