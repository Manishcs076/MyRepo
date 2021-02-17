num = int(input("Enter number"))
def collatz(num):
    #num = int(input("Enter the number"))
    if num%2==0:
        print(num//2)
    elif num%2!= 0:
        print(3 * num + 1)
collatz(num)           
collatz(round(num/2))