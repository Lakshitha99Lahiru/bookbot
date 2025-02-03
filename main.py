def count_letters(text):
    lowered_text = text.lower()
    letter_count = {}
    for letter in lowered_text:
        if letter in letter_count:
            previous_letter_count = letter_count[letter]
            letter_count[letter] = previous_letter_count + 1
        else:
            letter_count[letter] = 1
        
    return letter_count

def letter_count_to_list(letter_count):
    letter_count_list = []
    for key in letter_count:
        new_dict = {'key' : key,  'value' : letter_count[key] }
        letter_count_list.append(new_dict)
    return letter_count_list

def sort_on(dict):
    return dict['value']

def count_words(text):
    words = text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letter_count = count_letters(file_contents)
        #print(letter_count)

        #converting the letterCount dictionary to a list of dictionaries

        letter_count_list = letter_count_to_list(letter_count)
       
        letter_count_list.sort(reverse=True, key=sort_on)

        print("--- Begin report of books/frankenstein.txt ---")
        word_count =count_words(file_contents)
        print(f"{word_count} words found in the document \n")
        
        for item in letter_count_list:
            
            letter = item['key']
            count = item['value']

            if letter.isalpha():
                print(f"The '{letter}' character was found {count} times")
            else:
                continue

        print("--- End report ---")
main()
