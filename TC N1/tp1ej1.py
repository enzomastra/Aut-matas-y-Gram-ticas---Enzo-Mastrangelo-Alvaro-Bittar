def validate(string):

    alnum=any(i.isalnum()for i in string)
    alpha=any(i.isalpha()for i in string)
    upper=any(i.isupper()for i in string)
    lower=any(i.islower()for i in string)
    digit=any(i.isdigit()for i in string)
    lenght=len(string) >=8

    return alnum, alpha, upper, lower, digit, lenght

string= input("Insert an string")
result=validate(string)
print (result)