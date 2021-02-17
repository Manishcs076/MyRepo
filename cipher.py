text = input("Enter Your Text")
list = []
list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list.append(text)
a = 0
for i in range(len(list[0])):
    if list[0][a] in list1:
            b = list1.index(list[0][a])+1
            if b == 26:
                print(list1[-b])
            else:
                print(list1[b])
    elif list[0][a] not in list1:
        print(list[0][a])
    a += 1
