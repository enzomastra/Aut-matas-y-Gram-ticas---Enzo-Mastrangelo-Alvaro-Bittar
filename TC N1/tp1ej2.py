def solve(string):
    sumate=[]
    nums=string.split()
    result=0

    if nums[1]!="*":
        result=nums[0]
        sumate.append(int(result))

    for i in range(len(nums)):
        if nums[i]=="*":
            result=int(nums[i - 1])*int(nums[i + 1])
            sumate.append(int(result))

        elif nums[i]=="+":
            if i+2< len(nums) and nums[i+2]=="*":
                pass
            else:
                result=nums[i+1]
                sumate.append(int(result))

    print(sum(sumate))


string = "2 + 7 * 2 + 1"
resultado = solve(string)