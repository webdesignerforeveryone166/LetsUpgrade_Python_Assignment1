# Question 1 to create two lists of some brand names.

list_1 = ['Apple','Google','Coco-Cola','Microsoft']
list_2 = ['Tesla','Amazon','Microsoft','Apple','Google']
print(list_1)
print(list_2)
print('Assignment_1 Question1 is completed.')

# Question 2 to create list of overlapping brands in both lists

Over_lapping_list = list()
for lst in list_1:
    if lst in list_2:
        Over_lapping_list.append(lst)

print("The overlapping elements of list 1 and list 2 in list 3 are:",Over_lapping_list)


# Question_3 To pring even numbers between 20 to 40

number = 20
while number<=40:
    if number%2==0:
        print(f'The {number} is even')
    else:
        print(f'The {number} is not even')

    number += 1

print('Done')