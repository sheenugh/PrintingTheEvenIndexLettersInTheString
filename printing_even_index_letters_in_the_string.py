


# >>>>>>>>>> PSEUDO CODE <<<<<<<<<<
# ---------- ACTUAL CODES ----------
# - Printing the sentence as "original string is .... and the word inputted"
characters = input("Enter a Word: ")
print("The original string is", characters)
print("\n")

# - Variable
characters_length = len(characters)

# - Printing the sentence "printing only even index number"
print("Printing the even index letters in the string.")

# This section is for looping na.
for i in range(0, characters_length, 2):
    print(characters[i])

