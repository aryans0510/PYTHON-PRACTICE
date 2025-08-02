print("Welcome to the ARYAN'S KBC Game!!!!")


level = input ("Enter your level (easy, medium, hard): ").strip().lower()
if level == "easy":
    question1 = "who is the current prime minister of India?"
    options1 = ["Narendra Modi", "Rahul Gandhi", "Amit Shah", "Sonia Gandhi"]
    correct_answer1 = "Narendra Modi"
    print (question1)
    for i, option in enumerate(options1, 1):
        print(f"{i}. {option}")
    answer1 = int(input("Enter the number of your answer: "))
    if options1[answer1 - 1] == correct_answer1:
        print("hurrray!!!CORRECT ANSWER YOU WON 500!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")




    question2 = "who is the current president of India?"
    options2 = ["Droupadi Murmu", "Ram Nath Kovind", "Pranab Mukherjee", "A.P.J. Abdul Kalam"]
    correct_answer2 = "Droupadi Murmu"
    print(question2)
    for i, option in enumerate(options2, 1):
        print(f"{i}. {option}")
    answer2 = int(input("Enter the number of your answer: "))
    if options2[answer2 - 1] == correct_answer2:
        print("hurrray!!!CORRECT ANSWER YOU WON 1000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")




    question3 = "who is the current chief minister of Maharashtra?"
    options3 = ["Eknath Shinde", "Uddhav Thackeray", "Devendra Fadnavis", "Ashok Chavan"]
    correct_answer3 = "Eknath Shinde"
    print(question3)
    for i, option in enumerate(options3, 1):
        print(f"{i}. {option}")
    answer3 = int(input("Enter the number of your answer: "))
    if options3[answer3 - 1] == correct_answer3:
        print("hurrray!!!CORRECT ANSWER YOU WON 2000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")


elif level == "medium":
    question1 = "who is the defence minister of india?"
    options1 = ["Narendra Modi", "Rahul Gandhi", "Amit Shah", "Sonia Gandhi"]
    correct_answer1 = "Amit Shah"
    print(question1)
    for i, option in enumerate(options1, 1):
        print(f"{i}. {option}")
    answer1 = int(input("Enter the number of your answer: "))
    if options1[answer1 - 1] == correct_answer1:
        print("hurrray!!!CORRECT ANSWER YOU WON 1000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")




    question2 = "Who is known as the 'Missile Man of India'??"
    options2 = ["Droupadi Murmu", "Ram Nath Kovind", "Pranab Mukherjee", "A.P.J. Abdul Kalam"]
    correct_answer2 = "A.P.J. Abdul Kalam"
    print(question2)
    for i, option in enumerate(options2, 1):
        print(f"{i}. {option}")
    answer2 = int(input("Enter the number of your answer: "))
    if options2[answer2 - 1] == correct_answer2:
        print("hurrray!!!CORRECT ANSWER YOU WON 2000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")




    question3 = "Which Indian city is known as the ‘Silicon Valley of India’?"
    options3 = ["Pune", "Hyderabad", "Bangalore", "Chennai"]
    correct_answer3 = "Bangalore"
    print(question3)
    for i, option in enumerate(options3, 1):
        print(f"{i}. {option}")
    answer3 = int(input("Enter the number of your answer: "))
    if options3[answer3 - 1] == correct_answer3:
        print("hurrray!!!CORRECT ANSWER YOU WON 4000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")





    question4 = "Which Indian state has the longest coastline?"
    options4 = ["Andhra Pradesh", "Maharashtra", "Tamil Nadu", "Gujarat"]
    correct_answer4 = "Gujarat"
    print(question4)
    for i, option in enumerate(options4, 1):
        print(f"{i}. {option}")
    answer4 = int(input("Enter the number of your answer: "))
    if options4[answer4 - 1] == correct_answer4:
        print("hurrray!!!CORRECT ANSWER YOU WON 5000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")




    question5 ="Who wrote ‘The Discovery of India’?"
    options5 = ["Jawaharlal Nehru", "Mahatma Gandhi", "B.R. Ambedkar", "Sardar Patel"]
    correct_answer5 = "Jawaharlal Nehru"
    print(question5)
    for i, option in enumerate(options5, 1):
        print(f"{i}. {option}")
    answer5 = int(input("Enter the number of your answer: "))
    if options5[answer5 - 1] == correct_answer5:
        print("hurrray!!!CORRECT ANSWER YOU WON 10000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")




  
elif level == "hard":
    question1 = "What was the name of the Mughal structure known as ‘Rauza-i-Munawwara’?"
    options1 = ["Taj Mahal", "Humayun's Tomb", "Red Fort", "Jama Masjid"]
    correct_answer1 = "Taj Mahal"
    print(question1)
    for i, option in enumerate(options1, 1):
        print(f"{i}. {option}")
    answer1 = int(input("Enter the number of your answer: "))
    if options1[answer1 - 1] == correct_answer1:
        print("hurrray!!!CORRECT ANSWER YOU WON 10000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")





    question2 = "Which Indian scientist is known for the Green Revolution?"
    options2 = ["M. S. Swaminathan", "C. V. Raman", "A. P. J. Abdul Kalam", "Vikram Sarabhai"]
    correct_answer2 = "M. S. Swaminathan"
    print(question2)
    for i, option in enumerate(options2, 1):
        print(f"{i}. {option}")
    answer2 = int(input("Enter the number of your answer: "))
    if options2[answer2 - 1] == correct_answer2:
        print("hurrray!!!CORRECT ANSWER YOU WON 20000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")






    question3 = "Who was the first Indian to win a Nobel Prize?"
    options3 = ["Rabindranath Tagore", "C. V. Raman", "Mother Teresa", "Amartya Sen"]
    correct_answer3 = "Rabindranath Tagore"
    print(question3)
    for i, option in enumerate(options3, 1):
        print(f"{i}. {option}")
    answer3 = int(input("Enter the number of your answer: "))
    if options3[answer3 - 1] == correct_answer3:
        print("hurrray!!!CORRECT ANSWER YOU WON 30000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")





    question4 = "Which Indian state is known as the ‘Land of Five Rivers’?"
    options4 = ["Punjab", "Haryana", "Bihar", "Uttar Pradesh"]
    correct_answer4 = "Punjab"  
    print(question4)
    for i, option in enumerate(options4, 1):        
        print(f"{i}. {option}")
    answer4 = int(input("Enter the number of your answer: "))
    if options4[answer4 - 1] == correct_answer4:
        print("hurrray!!!CORRECT ANSWER YOU WON 50000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")






    question5 = "Who wrote the Indian National Song ‘Vande Mataram’?"
    options5 = ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Allama Iqbal", "Lata Mangeshkar"]
    correct_answer5 = "Bankim Chandra Chatterjee"
    print(question5)
    for i, option in enumerate(options5, 1):
        print(f"{i}. {option}")
    answer5 = int(input("Enter the number of your answer: "))
    if options5[answer5 - 1] == correct_answer5:
        print("hurrray!!!CORRECT ANSWER YOU WON 100000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")







    question6 = "Which Indian leader is known as the ‘Iron Man of India’?"
    options6 = ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "B.R. Ambedkar"]
    correct_answer6 = "Sardar Vallabhbhai Patel"
    print(question6)
    for i, option in enumerate(options6, 1):
        print(f"{i}. {option}")
    answer6 = int(input("Enter the number of your answer: "))
    if options6[answer6 - 1] == correct_answer6:
        print("hurrray!!!CORRECT ANSWER YOU WON 200000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")







    question7 = "Which is the longest dam in India and in which state is it located?"
    options7 = ["Bhakra Nangal Dam, Himachal Pradesh", "Sardar Sarovar Dam, Gujarat", "Hirakud Dam, Odisha", "Tehri Dam, Uttarakhand"]
    correct_answer7 = "Hirakud Dam, Odisha"
    print(question7)
    for i, option in enumerate(options7, 1):
        print(f"{i}. {option}")
    answer7 = int(input("Enter the number of your answer: "))
    if options7[answer7 - 1] == correct_answer7:
        print("hurrray!!!CORRECT ANSWER YOU WON 500000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")
        





    question8 = "Who designed the National Flag of India?"
    options8 = ["Pingali Venkayya", "B.R. Ambedkar", "Mahatma Gandhi", "Jawaharlal Nehru"]
    correct_answer8 = "Pingali Venkayya"
    print(question8)
    for i, option in enumerate(options8, 1):
        print(f"{i}. {option}")
    answer8 = int(input("Enter the number of your answer: "))
    if options8[answer8 - 1] == correct_answer8:
        print("hurrray!!!CORRECT ANSWER YOU WON 1000000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")






    question9 = "Which Indian state is known as the ‘Land of Festivals’?"
    options9 = ["Assam", "Kerala", "West Bengal", "Tamil Nadu"]
    correct_answer9 = "Assam"
    print(question9)
    for i, option in enumerate(options9, 1):
        print(f"{i}. {option}")
    answer9 = int(input("Enter the number of your answer: "))
    if options9[answer9 - 1] == correct_answer9:
        print("hurrray!!!CORRECT ANSWER YOU WON 2000000!!!")
    else:
        print("Sorry, that's incorrect. Better luck next time!")
        
        



    question10 = "What is the land boundary length of India?"
    options10 = ["15,106 km", "20,000 km", "22,000 km", "25,000 km"]
    correct_answer10 = "15,106 km"  
    print(question10)
    for i, option in enumerate(options10, 1):
        print(f"{i}. {option}")
    answer10 = int(input("Enter the number of your answer: "))
    if options10[answer10 - 1] == correct_answer10:
        print("hurrray!!!CORRECT ANSWER YOU WON 5000000!!!")
    else:   
        print("Sorry, that's incorrect. Better luck next time!")

    print("Congratulations! You have completed the KBC game at the hard level!")

