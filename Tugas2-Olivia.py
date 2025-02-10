secret_word = "slay"
ans = (["_"] * len(secret_word))
list=[]
attempt=6
while True:
    print("answer:"," ".join(ans))
    x = input("Enter a letter: ").lower()
    if x in list:
        print("Still have ",attempt,"attempt")
        continue
    else:
        attempt=attempt-1
        print("have",attempt,"attempt")
    if attempt<=0:
        print("done")
        print('you lose')
        break
    list.append(x)
    print(list)
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
            print('you win')
            break
    else:
        print("Wrong guess.Try again")
