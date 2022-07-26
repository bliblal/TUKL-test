def solve(arr):
    #creating a function paramater for N fails the test
    #extrapolating length from the array constructed 
    n=len(arr)
    tinp=arr

    count=0
    for i in range(n):
        for j in range(i+1,n):
            print(tinp[i])
            print(tinp[j])
            print("------------")
            if tinp[i]<tinp[j]:
                break
            if tinp[i]>=tinp[j]:
                if tinp[i]==tinp[j]:
                    print("^^^^^^^")
                    count+=1
                    print("(%i,%i)"%(tinp[i],tinp[j]))
    #since each path also goes backward, it effectively counts as 2
    count*=2
    return count

arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = solve(arr)