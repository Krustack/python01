#สร้างfunction
def hello():
    print("hello function")
    
#เรียกใช้function
hello()
#ฟังก์ชั่นแบบส่งค่าผ่าน parameter
def helloName(name):
     print("hello",name)
helloName("Wisanu")
def grade(name,score):
     if score>=80:
        print(name,"grade A")
     elif score>=70:
        print(name,"grade B")
     elif score>=60:
        print(name,"grade C")
     elif score>=50:
        print(name,"grade D")
     else:
        print(name,"grade F")
grade("wisanu",80)
grade("soranun",49)
grade("weerapat",70)
#returnค่ากลับ
def sumScore(score1,score2,score3,score4,score5):
   sum =score1+score2+score3+score4+score5
   return sum
grade("wisanu",sumScore(20,18,17,19,15))