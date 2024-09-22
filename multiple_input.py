# # Using List Comprehension
# num_inputs = int(input('Enter the number of inputs: '))
# user_inputs = [input('Enter input {i + 1}: ') for i in range(num_inputs)]

# print('User inputs:', user_inputs)

test_list = [int(input("Enter number")) for i in range(5)]
print(test_list)

for i in range(0,len(test_list)):
    constant = ""
    # print("%d %d:"%i%test_list[i])
    if(test_list[i] == 0 ): 
        constant = "*"
    elif (test_list[i] == 1):
        constant = "***"
    elif (test_list[i] == -100):
        constant = "**"
    else :
        constant = ""
    
    print("%d:"%i,constant)