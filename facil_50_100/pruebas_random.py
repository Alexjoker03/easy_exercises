import random

lives = 3
word = ["Toy Story", "Monsters inc", "El Lorax", "Mulan", "Star Wars"]
word_missing = ["T__ St_r_", "M_n__er_ _n_", "El L__a_", "M___n", "St__ W___"]
word_to_guess = random.choice(word_missing) 
index_position = word_missing.index(word_to_guess)
word_to_compare_to = word[index_position]


word_to_guess_2 = []
for i in word_to_guess:
    word_to_guess_2.append(i)

print(word_to_guess)
print(word_to_guess[-1])

    


