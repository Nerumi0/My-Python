sum = 0
def Ex(n):
    total_sum = 0
    for i in range(n):
        score = int(input("คะแนนนักศึกษา %d: " % (i+1)))
        total_sum += score
    average = total_sum / n
    return average
    
n = int(input("จำนวนนักศึกษา: "))
print("คะแนนเฉลี่ยของนักศึกษา: %.2f" % Ex(n))

    
    
    