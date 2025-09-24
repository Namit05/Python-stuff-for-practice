#Quiz game

questions=("What is my name? :",
           "What is my age? :",
           "What is my fav food? :",
           "What is my fav subject? :")
    
options=(("A. Timan" , "B. Namit", "C. Rasan", "D. Utkarsh"),
         ("A. 17","B. 18","C. 19","D. 20"),
         ("A. Pizza" ,"B . Burger", "C. Biryani", "D. PaniPuri"),
         ("A. Biology", "B.Physics", "C. English", "D. Chemistry"))

answers=("B","C","A","A")
guesses=[]
score=0
question_num=0

for question in questions :
    print("--------")
    print(question)
    for option in options(question_num) :
        score+=1
        print("Correct!")




