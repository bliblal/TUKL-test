#check if string is even

def anagram(s):
    strlen=len(s)
    print(strlen)

    if strlen%2!=0:
        print("string does not have evn no. of letters")
        return -1
    hstrlen=strlen//2
    print("half-length:",hstrlen)

    s1=s[hstrlen:]
    s2=s[:hstrlen]
    print("string 1-",s1)
    print("string 2-",s2)
    d1=dict()
    d2=dict()
    for alpha in s1:
        d1[alpha]=d1.get(alpha,0)+1
        
    for alphas in s2:
        d2[alphas]=d2.get(alphas,0)+1

    print(d1)
    print("--------------")
    print(d2)

    if d1==d2:
        print("dictionaries equal")
        return -1
    diff=0
    for key in d1:
        if key in d2:
            print("key:",key)
            delta=(d1.get(key))-(d2.get(key))
            if delta>0:
                diff+=delta
        else:
            diff+=(d1.get(key))
        print("current",diff)
    print("final",diff)
    
s=input("enter the string")
print(anagram(s))

