import json

with open('questions.json', 'r') as file:
    content = file.read()
    
   
data = json.loads(content) 


for question in data:
    print(question['question_text'])
    for index, options in enumerate(question["alternatives"]):
        print(index +1,"-", options)
    user_answer = int(input("Enter your answer as numer"))
    question["user_answer"] = user_answer

       
        
score=0
for index, question in enumerate(data):
    if question["correct_anser"] == question["user_answer"]:
         score= score+1
         result = "Correct answer"
    else:
        result = "Wroung answer"
        
    
    
    message=f"{result} {index+1} - your answer is {question['user_answer']},"\
        f"Correct answer:{question['correct_anser']}"
    print(message)
    
print(score,"/",len(data))