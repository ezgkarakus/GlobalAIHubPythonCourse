questions = {"1: What nationality is David Beckham?" : "english",
             "2: What is the Capital of Turkey?": "ankara",
             "3: Where is the Anıtkabir?:" : "ankara",
             "4: Who wrote The Metamorphosis ?": "franz kafka",
             "5: When is Halloween? ": "31st october",
             "6:What is the eighth month of the year?": "august",
             "7: What is the currency in Japan?": "japanese yen",
             "8: Which year did Mustafa Kemal Atatürk died?": "1938",
             "9: Where is the head office of the Global IA Hub": "switzerland",
             "10: -What does WHO stand for?": "world health organisation"}
score = 0
for question, answer in questions.items():
    print(f"QUESTION {question}")
    user_answer = input().lower()
    if user_answer == answer:
        score += 10

if score <= 50:
    print(f"!YOU LOST!{score}")
elif score > 50:
    print(f"!YOU WON! SCORE:{score}")
