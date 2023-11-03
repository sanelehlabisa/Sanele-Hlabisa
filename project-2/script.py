
while True:
    user_input = input("Please enter a five digit number : ")
    
    if (not user_input.isdigit()) or len(user_input) != 5:
        print("Please try again")
    else:
        break
    
number =  int(user_input)
reversed_number = 0
sum = 0
added_number = 0


while number != 0:
    print(number)
    num = number % 10
    reversed_number = reversed_number * 10 + num
    sum += num
    added_number = added_number/ 10  + (num + 1)  
    number //= 10
added_number = int(added_number * 10e3)
print("The reversed number is\t:", reversed_number)
print("The sum of numbers is\t:", sum)
print("The added number is\t:", added_number)