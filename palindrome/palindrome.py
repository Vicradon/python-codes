def palindrome(str):
    palindromeArr = []
    strArr = list(map(lambda x: x.lower(), str.split()))
    
    for i in strArr:
        if len(i) % 2 != 0:
            workWith = len(i) // 2
            
            if i[0:workWith] == i[workWith+1: workWith * 2 + 1][::-1]:
                palindromeArr.append(i)
                
    if len(palindromeArr) > 0:
        return max(palindromeArr)
    
    return "No Palindrome"

print(palindrome("Madam Adora teaches Malayalam"))
