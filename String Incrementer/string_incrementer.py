"""
URL: https://codewars.com/kata/54a91a4883a7de5d7800009c/train/python
Author: Sahil Bhimjiani
Email: sahil9701@gmail.com
"""
def increment_string(strng):
    if strng!="":
        if strng[-1].isnumeric():
            a=""
            for idx,item in enumerate(strng[::-1]):
                
                if item.isnumeric():
                    a+=item
                else:
                    break
            a=a[::-1]
            new_string=strng[:strng.find(a)]+str(int(a)+1)
            return strng[:strng.find(a)]+(len(strng)-len(new_string))*'0'+str(int(a)+1)
            
        else:
            return strng+str("1")
    return "1"
