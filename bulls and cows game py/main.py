from random import randint
#"Бык" означает, что цифра угадана и стоит на правильной позиции.
#"Корова" означает, что цифра угадана, но стоит не на правильной позиции.
def game_bulls_cows(num1,count=1):
    num1= str(num1)
    print(num1)
    cow = 0
    bull = 0
    while(True):
        num2 = input("Введите число , которое загадал компьютер : ")
        if(len(num2) == 4):
            break
        else:
            print("Вы ввели не 4-х значное число ! ")
    if(num1 != num2):
        bulls_list = []
        for i in range(0,4):
            if(num1[i] == num2[i]):
                bulls_list.append(num1[i])
                bull +=1
        cows_list = []
        for i in range(0,4):
            for j in range(0,4):
                if(num2[i] == num1[j] and i != j):
                    net = True
                    for k in range (0,len(cows_list)):
                        if(num2[i] == cows_list[k]):
                            net = False
                    if(net):
                        for l in range(0,len(bulls_list)):
                            if(num2[i] == bulls_list[l]):
                                net = False
                        if(net):
                            cows_list.append(num2[i])
                            cow+=1


        print("bull : ",bull)
        print("cow : ",cow)
        return game_bulls_cows(num1,count+1)
    else:
        print("bull : ",4)
        return count
    
if __name__ == "__main__":
       
    print("Задание 2")
    num1 = randint(1000,9999)
    print("Количество попыток : " ,game_bulls_cows(num1))