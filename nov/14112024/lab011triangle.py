s1=int(input("one side "))
s2=int(input("two side"))
s3=int(input("three side"))
if s1== s2 == s3:
    print("equliteral triangle")
elif (s1==s2!=s3)or(s1!=s3==s2)or(s1==s3!=s2):
    print("isoceles triangle")
else:
    print("scalene triangle")
