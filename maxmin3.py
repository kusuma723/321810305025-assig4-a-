st=[]
num=int(input("how many numbers:"))
for n in range(num):
    numbers=int(input("Enter the number"))

    st.append(numbers)
print("Maximum element in the list:",max(st),"\nMinimum element in the list is:",min(st))
