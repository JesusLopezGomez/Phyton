for num in range (1, 101):
        
    if (num%13 == 0) and (num%7 == 0):
        print(f"{num} Es múltiplo de 13 y 7")
        
    elif (num%7 == 0):
        print(f"{num} Es múltiplo de 7")
        
    elif (num%13 == 0):
        print(f"{num} Es múltiplo de 13")
        
    else:
        print(num)
            

        