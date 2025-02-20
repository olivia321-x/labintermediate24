import random
secret_word=['satu','dua','tiga','empat','lima','enam','tujuh']
score=0
def main(secret_word):
    global score
    choose=random.choice(secret_word)
    secret_word.remove(choose)
    ans = (["_"] * len(choose))
    list=[]
    attempt=6
    def updatetext(attempt,ans,secret_word,list):
        global score
        while True:
            print("answer:"," ".join(ans))
            x = input("Enter a letter: ").lower()
            if x in list:
                print("Still have ",attempt,"attempt")
                continue
            else:
                print("have",attempt,"attempt")
            if attempt<=0:
                print("done")
                print('You lose')
                break
            list.append(x)
            print(list)
            if not x.isalpha():
                print("invalid letter")
                continue
            if x in choose:
                for i in range(len(choose)):
                    if choose[i] == x:       
                        ans[i] = x 
                print("Good job")
                if "_" not in ans:
                    print('Congratulations! You complete the task','"',choose,'"')
                    print('You win')
                    score=score+1
                    break
            else:
                attempt=attempt-1
                print("Wrong guess.Try again")
    updatetext(attempt,ans,secret_word,list)
def lanjut():
    global score
    while True:
        pilih=input("Main lagi? ya/tidak :")
        if pilih.lower()=='ya':
            main(secret_word)
        elif pilih.lower()=='tidak':
            print("nice try")
            print("Your score:",score)    
            break
        else:
            print("invalid") 
            
main(secret_word)
lanjut()
