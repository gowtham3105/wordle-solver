import json
class Word:

    def __init__(self, word):
        self.neighbours = []
        self.word=word
        self.fixed_letter_positions = {}
        self.letter_present_list=[]
        self.letter_not_present_list=[]
        self.not_fixed_letter_positions = {}
        fi = open('words_alpha_5.txt', 'r')
        for line in fi.readlines():
            word = line.strip('\n')
            self.neighbours.append(word)
        

    def filter_words(self):
        # wordss = ['apple', 'applr', 'appln', 'applt', 'apptt', 'attrp', 'trtra']
        neighbours = []
        keys = [0,1,2,3,4]
        for i in self.fixed_letter_positions.keys():
            if i in keys:
                keys.remove(i)
            
        for i in keys:
            if self.word[i] in self.letter_present_list:
                if i not in self.not_fixed_letter_positions:
                    self.not_fixed_letter_positions[i] = [self.word[i],]
                else:
                    self.not_fixed_letter_positions[i].append(self.word[i])

        print(self.not_fixed_letter_positions)

        for word in self.neighbours:
            word = word.strip('\n')
            word_quit = False
                        
            for pos, letter in self.fixed_letter_positions.items():
                # print(pos, letter, word[pos])
                if word[pos] != letter:
                    word_quit = True
                    break
            
            if word_quit:
                # print("word quit111", word)
                continue
                
            # for pos, letter in self.not_fixed_letter_postions.items():
            #     if word[pos] == letter:
            #         word_quit=True
            #         break   
                    
            # if word_quit:
            #     # print("word quit111", word)
            #     continue


            word_list = list(word)
            for i in self.letter_present_list:
                if i not in word_list:
                    word_quit = True
                    break
            
            if word_quit:
                # print("word quit111", word)
                continue
            
           
                    
            for i in range(len(word)):
                if i in self.not_fixed_letter_positions.keys():
                    if word[i] in self.not_fixed_letter_positions[i]:
                        word_quit=True
                        break         
            
            if word_quit:
                continue
            
           
            for letter in self.letter_not_present_list:
                print(self.letter_not_present_list)
                if letter in word:
                    word_quit = True
                    break

            if word_quit:
                continue
            
            neighbours.append(word)
            # print(word)
        self.neighbours = neighbours
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
            # print(neighbour, heuristic)
            if heuristic > best_heuristic:
                best_heuristic = heuristic
                best_word = neighbour
        self.word = best_word
        return best_word    



def main():
    initial_word = input("Enter the Initial Word: ")
    
    
    # not_fixed_letters_positions = {}
    word = Word(initial_word)

    tries = 0
    while(tries<6):
        fixed_letter_str = input("Enter the fixed_letters(in the example format _a_c_): ")
        # not_fixed_letter_str = input("Enter the not_fixed_letter(in the example format _b_d_): ")

        for i in range(len(fixed_letter_str)):
            if fixed_letter_str[i] != '_':
                word.fixed_letter_positions[i] = initial_word[i]
            
        
        word.letter_present_list  = list(map(str.lower, input("Enter the letters present in the word (in the example format a c ): ").split(' ')))
        word.letter_not_present_list.extend(list(map(str.lower, input("Enter the letters not present in the word (in the example format a c ): ").split(' '))))
        word.filter_words()
        print(word.choose_next_word())
       
        tries += 1


main()
