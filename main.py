"""READ ME!!!

The next task is to update recommendations from second iterations if there are a lot of options
implement a new list to show the list(or dict with priority) of words in priority order to show what gives the maximum entropy

Refer 3Blue1Brown youtube video to better understand entropy, choosing the most probable solution

Check letter frequency (In 5 letter words if possible)
write a program for the above using words.txt as a source to find the letter frequency

nvm formulate an algorithm to find at what iteration what word is suitable whether it should select from the possible words or from all words which  contains the maximum number needed letter details
"""


from entro import findBest


#from loader import load_words
def load_words(filename="words.txt"):
    # Loads words from a text file into a set
    with open(filename, "r") as f:
        return {line.strip().upper() for line in f}  # Set
word_list = load_words()# Set of all words

word_length = 5
chances = 6
while True:
    first_word = {5:"CRANE"}
    possible_words = word_list
    wrong_position = {}  # letter: [indexes]
    true_word = ['_', '_', '_', '_', '_']
    current_grid = []
    colouring = []
    discarded_letters = []

    print("----------------------------------")
    for i in range (chances):
        print("")
        if i == 0 and word_length == 5:
            print(f"Recommended starting word : {first_word[word_length]}")
        else:
            print("Possible words: ")
            if len(possible_words) > 400:
                print("400+")
            elif len(possible_words) == 0:
                print("None!")
            else:
                print(possible_words)
                if len(possible_words) > 2:
                    findBest(possible_words)
        print(true_word)
        if len(possible_words) == 1:
            break
        

        print(">>>", end = '')
        current_grid.append(input().upper())
        print(">>>", end = '')
        colouring.append(input().upper())
        
        # constraints
        for j in range (word_length):
            if colouring[i][j] == 'G':
                true_word[j] = current_grid[i][j]
            elif colouring[i][j] == 'O':
                wrong_position.setdefault(current_grid[i][j], []).append(j) 
        for j in range (word_length):
            if (colouring[i][j] != 'G') and (colouring[i][j] != 'O'):
                if (current_grid[i][j] not in true_word) and (current_grid[i][j] not in wrong_position):
                    discarded_letters.append(current_grid[i][j])
        
        
        # Narrowing
        new_possible_words = set()
        for word in possible_words:
            flag = True
            for letter_index in range(word_length):
                # Green letters
                if true_word[letter_index] != '_' and true_word[letter_index] != word[letter_index]:
                    flag = False
                    break
                
                # Orange letters are in the word?
                """ if word[letter_index] not in wrong_position:
                    flag = False
                    break """
                
                # Grey letters
                if word[letter_index] in discarded_letters:
                    flag = False
                    break
                
            if not flag:
                continue
            
            # Checking if wrong index values are present at that index
            for key in wrong_position:
                if key not in word:
                    flag = False
                    break
                for value in wrong_position[key]:
                    if word[value] == key:
                        flag = False
                        break
                    
            if flag:
                new_possible_words.add(word)
        possible_words = new_possible_words
            
        
                
            
                
                
    
        
