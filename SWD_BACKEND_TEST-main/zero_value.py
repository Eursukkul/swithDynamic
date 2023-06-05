"""เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว"""

def count_zero(n):
    count = 0
    i = 5
    while i //n >= 1:
        count +=n //i
        i *= 5
    return count

number = int(input("ป้อนตัวเลขที่ต้องการหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial: "))

if number >= 0:
    factorial = count_zero(number)
    print(f"ตัวเลข {number}! มีจำนวนเลข 0 ที่อยู่ติดกันหลังสุด {factorial} ตัว")
else:
    print("กรุณาป้อนตัวเลขที่มีค่ามากกว่าหรือเท่ากับ 0")