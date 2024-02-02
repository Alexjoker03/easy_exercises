import random



lives = 3
word = ["Toy Story", "Monsters inc", "El Lorax", "Mulan", "Star Wars"]
word_to_guess = random.choice(word)
word_to_guess_in_list = []
for i in word_to_guess:
    word_to_guess_in_list.append(i)


for i in range(((len(word_to_guess_in_list)//2) -1)):
    index_letter_to_be_hide = random.randint(0, len(word_to_guess_in_list))
    if word_to_guess_in_list[index_letter_to_be_hide - 1] != " ":
        word_to_guess_in_list[index_letter_to_be_hide - 1] = "_"
    else:
        pass    

print("----------------------------")
s = ''.join(word_to_guess_in_list)
print(s)
print("----------------------------")
 







"""index_position = word_missing.index(word_to_guess)
word_to_compare_to = word[index_position]


word_to_guess_2 = []
for i in word_to_guess:
    word_to_guess_2.append(i)

print(word_to_guess)
print(word_to_guess[-1])"""

    


