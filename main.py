import json
from re import T
class Word:

    def __init__(self, word):
        self.neighbours = []
        self.word=word
        self.fixed_letter_positions = {}
        self.letter_present_list=[]
        self.letter_not_present_list=[]
        self.not_fixed_letter_positions = {}
        fi = open('wordle_words_5.txt', 'r')
        for line in fi.readlines():
            word = line.strip('\n')
            self.neighbours.append(word)

    def filter_words(self):
        neighbours = []

        for word in self.neighbours:
            word = word.strip('\n')
            word_quit = False
                        
            for pos, letter in self.fixed_letter_positions.items():
                if word[pos] != letter:
                    word_quit = True
                    break
            
            if word_quit:
                continue

            word_list = list(word)
            for i in self.letter_present_list:
                if i not in word_list:
                    word_quit = True
                    break
            
            if word_quit:
                continue
                    
            for i in range(len(word)):
                if i in self.not_fixed_letter_positions.keys():
                    if word[i] in self.not_fixed_letter_positions[i]:
                        word_quit=True
                        break         
            
            if word_quit:
                continue
            
            for letter in self.letter_not_present_list:
                if letter in word:
                    word_quit = True
                    break

            if word_quit:
                continue
            
            neighbours.append(word)
        neighbours.sort()
        self.neighbours = neighbours
        print(neighbours)
        return neighbours


    def choose_next_word(self):
        # read dict from file
        fi = open('letter_frequency.json', 'r')
        frequency_matrix = json.load(fi)
        fi.close()
        best_heuristic = 0
        best_word = ''
        for neighbour in self.neighbours:
            heuristic=0
            for i in range(len(neighbour)):
                heuristic+=frequency_matrix[i][neighbour[i]]
            if heuristic > best_heuristic:
                best_heuristic = heuristic
                best_word = neighbour
                print("best_word", best_word)
        self.word = best_word
        return best_word    



def main():
    
    best_word = ""
    best_heuristic = 0
    fi = open('letter_frequency.json', 'r')
    frequency_matrix = json.load(fi)
    fi.close()
    fi = open('wordle_words_5.txt', 'r')
    for line in fi.readlines():
        word = line.strip('\n')
        heuristic=0
        for i in range(len(word)):
            heuristic+=frequency_matrix[i][word[i]]
        if heuristic > best_heuristic:
            best_heuristic = heuristic
            best_word =word
    print("best initial word", best_word)
    initial_word=best_word                       

    
    
    word = Word(initial_word)

    tries = 0
    while(tries<6 and len(word.neighbours)>1):
        fixed_letter_str = input("Enter the fixed_letters(in the example format _a_c_): ")

        for i in range(len(fixed_letter_str)):
            if fixed_letter_str[i] != '_':
                word.fixed_letter_positions[i] = word.word[i]
            
        print("Fixed Letter Positions: ",word.fixed_letter_positions)
        letter_present_str  = input("Enter the letters present in the word (in the example format a_c_ ): ")
        letter_present_dict = {}

        for i in range(len(letter_present_str)):
            if letter_present_str[i] != '_':
                letter_present_dict[i] = word.word[i]


        word.letter_present_list = letter_present_dict.values()
        
        print(letter_present_dict)
        not_fixed_list = word.not_fixed_letter_positions

        for key in letter_present_dict:
            if key not in word.fixed_letter_positions:
                if key not in not_fixed_list:
                    not_fixed_list[key] = [letter_present_dict[key],]
                else:
                    not_fixed_list[key].append(letter_present_dict[key])
        
        print("Not Fixed List:", not_fixed_list)
        
        word.not_fixed_letter_positions = not_fixed_list
        
        
        word.letter_not_present_list.extend(list(map(str.lower, input("Enter the letters not present in the word (in the example format a c ): ").split(' '))))
        word.filter_words()
        print(word.choose_next_word())
       
        tries += 1


main()

