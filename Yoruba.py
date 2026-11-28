# Tiv to Yoruba Language Translator

tiv_to_yoruba = {
    "M sugh": "Ẹ ṣé",
    "M ngu": "Mo wà níbí",
    "Aondo": "Ọlọ́run",
    "Mnyam": "Ẹranko",
    "Wa": "Wá"
}

print("WELCOME TO TIV TO YORUBA TRANSLATOR")
print("-----------------------------------")

print("Available Tiv Words:")

for word in tiv_to_yoruba:
    print(word)

while True:
    word = input("\nEnter a Tiv word: ")

    if word in tiv_to_yoruba:
        print("Yoruba Translation:", tiv_to_yoruba[word])
    else:
        print("Word not found in the dictionary.")

    choice = input("\nDo you want to translate another word? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using the translator!")
        break