a = 150
b = 100
if a>b:
     print(a)
#มีเงื่อนไข 2 อย่าง
score=30
if score>=50:
     print("test pass")
else:
     print("test fail")
#ternary
score=60
print("test pass") if score>=50 else print("test fail")
#มีมากกว่า 2 เงื่อนไข ใช้elif  กำหนดเงื่อนไข
scores = 52
if scores>=80:
     print("grade A")
elif scores>=70:
     print("grade B")
elif scores>=60:
     print("grade C")
elif scores>=50:
     print("grade D")
else:
     print("grade F")
