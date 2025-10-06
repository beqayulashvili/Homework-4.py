numbers = [1,2,3,4,5,6,7,8]

length = len(numbers)

total = sum(numbers)

print("რიცხვებიs სია:",numbers)
print("რიცხვების სიგრძე:",len(numbers))
print("რიცხვების ჯამი:", sum(numbers))
print("რიცხვების საშუალო:", total / length)

max_number = max(numbers)
min_number = min(numbers)
print("მაქსიმალური რიცხვი:", max_number)
print("მინიმალური რიცხვი:", min_number)

#დავალება 2

#import datetime

#temperatures = [33, 35, 28, 40, 29, 45, 41, 42]

#starrt_date = datetime.date(2025, 10, 6)

#s = 0 

#for i in range(len(temperatures)):
    # print(f"{starrt_date.strftime('%d/%m/%Y (%A)')}: {temperatures}")
    # starrt_date += datetime.timedelta(days=1)
     #s += temperatures 

     #გავიჭედე ყველა ტემპერატურას ყველა დღეზე მიჩვენებს 

#დავალება 3



#დავალება 4
for i in range(1, 50):
     if i % 3 == 0:
          continue
     if i % 7 == 0 and i > 30:
          print("ვიპოვე:",i)
          break

#დავალება 5

while True:
     while True:
          user_input = input("ჩაწერეთ რიცხვი 1:")
          if user_input.isdigit():
               number1 = int(user_input)
               break
          else:
                print("გთხოვთ ჩაწეროთ მხოლოდ რიცხვი.")

     while True: 
            user_input = input("რა მოქმედება გსურთ შეასრულოთ (+, -, *, /):")
            if user_input in ['+', '-', '*', '/']:
                 operation = user_input
                 break
            else:
                 print("გთხოვთ შეიყვანოთ მხოლოდ +, -, *, /")

     while True:
          user_input = input("ჩაწერეთ რიცხვი 2:")
          if user_input.isdigit():
               number2 = int(user_input)
               break
          else:
                print("გთხოვთ ჩაწეროთ მხოლოდ რიცხვი.")

     if operation == "+":
          print (number1 + number2)
     if operation == "-":
          print (number1 - number2)
     if operation == "*":
          print (number1 * number2)
     if operation == "/":
          print (number1 / number2)
      
#ვეღარ ვაჩერებ 
                 