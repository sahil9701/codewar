"""
URL: https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python
Author: Sahil Bhimjiani
Email: sahil9701@gmail.com
"""
formula='Mg21(Oh21)2'
#formula='H2O'
#formula='K4[ON)SO3)2]2'
formula="("+formula+")"
temp_dict={}
def check_function(new):
    for idx1,j in enumerate(new):
                    if j.isalpha():
                        if j.isupper():
                            if j not in temp_dict:
                                temp_dict[j]=1
                            else:
                                temp_dict[j]+=1
                            previous_attom=j
                        else:
                            new_attom=new[idx1-1]+j
                            previous_attom=new_attom
                            new_value=temp_dict[new[idx1-1]]
                            temp_dict[new_attom]=new_value
                            del temp_dict[new[idx1-1]]
                    elif j.isnumeric():
                        if not new[idx1-1].isnumeric():
                            temp_dict[previous_attom]*=(int(j))
                        else:
                            temp_dict[previous_attom]//=int(new[idx1-1])
                            temp_dict[previous_attom]*=(int(new[idx1-1]+j))
while '(' in formula or '[' in formula or '{' in formula:
    for idx,i in enumerate(formula):
        try:
            if i==')' and (formula[idx+1]).isnumeric():
                x=formula[:idx].rfind('(')
                new=formula[x+1:idx]
                check_function(new)
                for v,w in temp_dict.items():
                    temp_dict[v]=w*int(formula[idx+1])
                formula=formula[:x]+formula[idx+2:]
                break
            
            elif i==']' and (formula[idx+1]).isnumeric():
                x=formula[:idx].rfind('[')
                new=formula[x+1:idx]
                check_function(new)
                for v,w in temp_dict.items():
                    temp_dict[v]=w*int(formula[idx+1])
                formula=formula[:x]+formula[idx+2:]
                break
            elif i=='}' and (formula[idx+1]).isnumeric():
                x=formula[:idx].rfind('{')
                new=formula[x+1:idx]
                check_function(new)
                for v,w in temp_dict.items():
                    temp_dict[v]=w*int(formula[idx+1])
                formula=formula[:x]+formula[idx+2:]
                break
        except IndexError:
            formula=formula[1:-1]
            check_function(formula)
                        
print(temp_dict)
