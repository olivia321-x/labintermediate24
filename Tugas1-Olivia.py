secret_word = "slay"
ans = (["_"] * len(secret_word))
while True:
    print("answer:"," ".join(ans))
    x = input("Enter a letter: ").lower()
    if not x.isalpha():
        print("invalid letter")
        continue
    if x in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == x:       
                ans[i] = x                
        print("Good job")
        if "_" not in ans:
            print('Congratulations! You complete the task','"',secret_word,'"')
            break
    else:
        print("Wrong guess.Try again")
