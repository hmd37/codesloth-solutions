def lemonade(bills: list[int]) -> bool:
    five, ten = 0, 0
    
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0: 
                return False
            five -= 1
            ten += 1 
        else:
            if ten > 0 and five > 0: 
                ten -= 1
                five -= 1
            elif five >= 3: 
                five -= 3
            else:
                return False 
    return True


print(lemonade([5, 5, 5, 10, 20])) 
print(lemonade([5, 5, 10, 10, 20]))  
print(lemonade([10, 10]))  
print(lemonade([5, 5, 10]))  


# For those who wants to learn new library:
from collections import Counter

def lemonade(bills: list[int]) -> bool:
    cash = Counter() 

    for bill in bills:
        if bill == 5:
            cash[5] += 1  
        elif bill == 10:
            if cash[5] == 0:  
                return False
            cash[5] -= 1
            cash[10] += 1  
        else:  
            if cash[10] > 0 and cash[5] > 0:  
                cash[10] -= 1
                cash[5] -= 1
            elif cash[5] >= 3: 
                cash[5] -= 3
            else:
                return False  

    return True


print(lemonade([5, 5, 5, 10, 20]))  
print(lemonade([5, 5, 10, 10, 20]))  
print(lemonade([10, 10])) 
print(lemonade([5, 5, 10]))  
