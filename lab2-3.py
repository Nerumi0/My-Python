print ("หาดัชนีมวลกาย BMI")
w = float (input("น้ำหนัก : "))
x = float (input("ส่วนสูง  : "))
h=(x/100)**2
n = w/h
print("ค่าดัชนีมวลกายคือ %.2f" %n)

if n<18.50:
    print("น้ำหนักน้อยผอม")
    
elif n>=18.50 and n<=22.90 :
    print("ปกติสุขภาพดี")
    
elif n <=24.90 and n>=23:
    print("ท้วน")
    
elif n>=25 and n <=29.90:
    print("อ้วน")
elif n >30:
        print("อ้วนมาก")