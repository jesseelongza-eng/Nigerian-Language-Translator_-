import hausa

while True:
    print("LANGUAGE TRANSLATOR")
    print("1. Hausa")

    choice = input("Select a language: ")

    if choice == "1":
        dictionary = hausa.english_to_hausa
        break
    else:
        print("Invalid choice. Please try again.")

print("\nENGLISH TO HAUSA TRANSLATION")

for english, translated in dictionary.items():
    print(f"{english} : {translated}")