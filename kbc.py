que=["what is my name?","what is my age?","who is my favourite player?"]
ans=["ankit",22,"virat kohli"]
sum=0

for i in range(len(que)):
    # print("answer for question ",i+1)
    print("Q:",i+1,que[i])
    ans1=input(f"please enter your answer for ques {i+1} ")
    if ans1==ans[i]:
        print("congratulations you anwered right question")
        sum+=1
    else:
        print("sorry wrong anwer")
   

print("you answer",sum,"questions right.")