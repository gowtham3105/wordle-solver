import sys
import os
import json


def make_json(file_name):
    # Open File
    english_dict = {}

    def add_word(word):
        curr_dict = english_dict
        for i in word:
            if i in curr_dict:
                curr_dict = curr_dict[i]
            else:
                curr_dict[i] = {"word": None}
                curr_dict = curr_dict[i]

        curr_dict["word"] = word

        return english_dict

    if not os.path.isfile(file_name):
        print("File Doesn't Exist")
        return False
    fi = open(file_name, "r")
    i = 0
    for word in fi.readlines():

        add_word(word.strip('\n'))
        i += 1

    out = open("my_dict.json", "w")
    json.dump(english_dict, out)
    out.close()
    fi.close()

    return english_dict, "my_dict.json"

def restrict_np_of_letters(file_name, n):
    fi = open(file_name, "r")
    data = fi.read()
    my_dict = json.loads(data)
    fi.close()
    def go_through_dict(dictionary, n):
        if n == 0:
            return dictionary
        new_dict = dictionary.copy()

        for key, item in new_dict.items():
            if key == "word":
                continue
            if n == 1:
                dictionary.pop(key)
            else:
                go_through_dict(dictionary[key], n-1)

        return dictionary

    my_dict = go_through_dict(my_dict, n)
    print(my_dict)
    out = open("my_dict_"+str(n)+".json", "w")
    json.dump(my_dict, out)
    out.close()


    return my_dict

def filter_words(no_of_letters):
    fi = open('words_alpha.txt', 'r')
    out = open('words_alpha_'+str(no_of_letters)+'.txt', 'w')


    for word in fi.readlines():
        if len(word.strip('\n')) == no_of_letters:
            out.writelines(word)
        else:
            continue




if __name__ == "__main__":

    fi = open("wordle_words.txt", "r")
    out = open("wordle_words_5.txt", "w")
    for line in fi.readlines():
        my_line = line.strip('\n')
        my_line = line.split(', ')
        # print(my_line)
        for word in my_line:
            new_word = word.replace('"', "")
            if len(new_word) == 5:
                out.writelines(new_word+'\n')
            else:
                continue
        
    
    out.close()
    fi.close()
