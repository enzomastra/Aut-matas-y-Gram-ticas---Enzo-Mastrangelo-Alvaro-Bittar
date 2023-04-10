def solve(string):
    sumate=[]
    nums=string.split("+")
    result=0

    for term in nums:
        if "*" in term:
            operation=term.split("*")
            product=1
            for num in operation:
                product*= int(num)
            sumate.append(product)
        else:
            sumate.append(int(term))
    print(sum(sumate))


string = "2 * 5 + 2 * 2 + 5"
resultado = solve(string)