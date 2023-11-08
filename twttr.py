text=input("Insert text: ")
space=""
characters = ['a', 'e' ,'i', 'o', 'u']
textlower = text.lower()
# for character in text: #dinushanka
#     # print(character)
#     if character in characters:
#         break

#     space += character
#     # characters = ""
#     # space += text + characters
# print(space) 

for character in text: #dinushanka
    # print(character)
    if character.lower() in characters:
        continue
    space += character
    # characters = ""
    # space += text + characters
print(space)    

# print(character)

# print(characters)


# def remove_vowels(text):
#     result = ""
#     for char in text:
#         if char not in "AEIOUaeiou":
#             result += char
#     return result

# def main():
#     user_input = input("Enter a text: ")
#     result = remove_vowels(user_input)
#     print("Text without vowels:", result)

# if __name__ == "__main__":
# main()
