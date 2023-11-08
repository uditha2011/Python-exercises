answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
answerformatchanged= answer.lower().replace("-", " ").replace("_"," ")

if answer== "42" or answerformatchanged== "forty two":
    print("Yes")  

else:
    print("No")