tiv_dictionary = {
    "M sugh": "Thank you",
    "M ngu": "I am here",
    "Aondo": "God",
    "Mnyam": "Animal",
    "Wa": "Come"
}

print("===== TIV TO ENGLISH TRANSLATOR =====")

while True:
    word = input("\nEnter a Tiv word (or type 'exit' to quit): ")

    if word.lower() == "exit":
        print("Thank you for using the translator!")
        break

    if word in tiv_dictionary:
        print("English meaning:", tiv_dictionary[word])
    else:
        print("Word not found in the dictionary.")