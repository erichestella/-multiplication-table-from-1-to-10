#adding up some title 
print('\n1-10 MULTIPLICATION TABLE\n')

#variable for the multiplication table
digits_numerical = [1,2,3,4,5,6,7,8,9,10]
digits_integers = [1,2,3,4,5,6,7,8,9,10]

#this function is to multiply the two variable given above 
for t in digits_numerical:
    for n in digits_integers:
        print(t * n, end= '\t')
    print()