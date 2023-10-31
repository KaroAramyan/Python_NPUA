def classify_numbers(arr):
    even_list = []
    odd_list = []
    for i in range(len(arr)):
        intuser_list = int(arr[i])
        if intuser_list % 2 == 0:
            even_list.append(intuser_list)
        else:
            odd_list.append(intuser_list)
    print("Even Numbers:", even_list)
    print("Odd Numbers:", odd_list)

user_str = input("Enter your numbers list: ")
user_list = user_str.split()
classify_numbers(user_list)
         