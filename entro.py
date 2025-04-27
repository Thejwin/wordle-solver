import math

def load_words(filename="words.txt"):
    with open(filename, "r") as f:
        return {line.strip().upper() for line in f}  # Set
word_list = load_words()


frequency = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

letter_frequency = {'A': 977, 'B': 282, 'C': 475, 'D': 393, 'E': 1233, 'F': 229, 'G': 311, 'H': 386, 'I': 670, 'J': 28, 'K': 210, 'L': 716, 'M': 316, 'N': 574, 'O': 756, 'P': 366, 'Q': 29, 'R': 900, 'S': 669, 'T': 731, 'U': 467, 'V': 152, 'W': 195, 'X': 37, 'Y': 423, 'Z': 40}

def wordle_coloring(guess: str, correct: str):
    if len(guess) != 5 or len(correct) != 5:
        raise ValueError("Both words must be exactly 5 letters long.")
    
    coloring = ["B"] * 5  
    correct_counts = {}  
    
    
    for letter in correct:
        correct_counts[letter] = correct_counts.get(letter, 0) + 1
    
   
    for i in range(5):
        if guess[i] == correct[i]:  
            coloring[i] = "G"
            correct_counts[guess[i]] -= 1  
    
    
    for i in range(5):
        if coloring[i] == "B" and guess[i] in correct_counts and correct_counts[guess[i]] > 0:
            coloring[i] = "O"
            correct_counts[guess[i]] -= 1  
    
    return "".join(coloring)


def filter_possible_words(correct: str, guess: str, color: str, wordSet: set):
    possible_words = set()
    
    for item in wordSet:
        if wordle_coloring(guess, item) == color:
            possible_words.add(item)
            
    return possible_words

def find_bit(wordSet: set, word: str, selected_word: str): # find the bit value for that word
    # compare word and selected word to form colouring
    color = wordle_coloring(selected_word, word)
    newSet = set()
    newSet = filter_possible_words(word, selected_word, color, wordSet)
    bit_value = math.sqrt(len(wordSet) / len(newSet))
    
    return bit_value
    

def compare_with_all(wordSet: set, word: str): # compare the assumed correct with all other words
    #compare with each word, assuming its the correct word to find its corresponding bit and average bit value
    bit_value_sum = 0
    for selected_word in wordSet:
        bit_value_sum += find_bit(wordSet, word, selected_word)
    
    avg_bit =  bit_value_sum / len(wordSet)
    return math.ceil(avg_bit * 1000) / 1000


def sort_on_bit(bit_list: list):
    l = len(bit_list)
    for i in range(l-1):
        for j in range(l - i - 1):
            if bit_list[j][1] < bit_list[j+1][1]:
                bit_list[j], bit_list[j+1] = bit_list[j+1], bit_list[j]


def findBest(wordSet: set): # Choose each word as assumed correct word
    bit_list = [] # word : bit/total bit
    for word in wordSet:
        bit_list.append([word, compare_with_all(wordSet, word)])

    sort_on_bit(bit_list)
    
    #PRINTING  
    for item in bit_list:
        print(f"{item[0]}: {item[1]}", end = "||")
    print()
    
