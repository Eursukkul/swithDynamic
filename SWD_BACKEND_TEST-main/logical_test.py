
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def convert_to_thai_text(number):
    thai_digits = ['ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
    thai_units = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

    if number == 0:
        return thai_digits[0]

    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number //= 10

    thai_text = ''
    for i, digit in enumerate(digits[::-1]):
        if digit != 0:
            if digit == 1 and i % 6 != 0:
                thai_text += thai_units[i % 6]
            else:
                thai_text += thai_digits[digit] + thai_units[i % 6]
        else:
            if i % 6 == 0 and i != 0 and digits[i - 1] != 0:
                thai_text += thai_units[i % 6]

    return thai_text[::-1]

number = int(input("ป้อนตัวเลขที่ต้องการแปลงเป็นภาษาไทย: "))
if 0 < number < 10000000:
    thai_text = convert_to_thai_text(number)
    print(f"ค่าของตัวเลข {number} เป็นภาษาไทยคือ \"{thai_text}\"")
else:
    print("กรุณาป้อนตัวเลขระหว่าง 1 ถึง 9,999,999")

