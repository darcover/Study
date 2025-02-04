s = input("Введите сжатую строку: ")  
result = ""  
i =0  

while i < len(s): 
     
    char =s[i]  
    i += 1  
    num = ""  
    while i < len(s) and s[i].isdigit(): 

        num +=s[i]  
        i +=1  
    count =int(num) if num else 1  
    result +=char * count  

print(result)