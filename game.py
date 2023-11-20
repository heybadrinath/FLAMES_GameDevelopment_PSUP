def flames_game(name1, name2):

    #dictionary to count each letter in names
    letter_count = {}
    

    for letter in name1:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    
    for letter in name2:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    

    total_count = sum(letter_count.values())
    
    # Calculate the number of common letters
    common_letters_count = 0
    for count in letter_count.values():
        if count > 1:
            common_letters_count += 1


    flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    relationship_index = (total_count - common_letters_count) % len(flames)
    relationship = flames[relationship_index]
    return relationship


print("************************************************")
name1 = input("Enter the first name: ").replace(" ", "").upper()
name2 = input("Enter the second name: ").replace(" ", "").upper()

result = flames_game(name1, name2)
print("The relationship between", name1, "and", name2, "is:", result)
print("************************************************")