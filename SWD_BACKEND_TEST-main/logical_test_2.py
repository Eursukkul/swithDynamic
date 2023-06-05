
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def num_to_roman(number):
    if number <= 0 or number > 1000:
        return "ค่าตัวเลขต้องอยู่ระหว่าง 1 ถึง 1000"
    
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    roman_number = ""
    for numeral, symbol in roman_numerals.items():
        while number >= numeral:
            roman_number += symbol
            number -= numeral

    return roman_number

number = int(input("ป้อนตัวเลขที่ต้องการแปลงเป็นตัวเลขโรมัน: "))

roman_number = num_to_roman(number)
print(f"ตัวเลข {number} แปลงเป็นตัวเลขโรมันคือ '{roman_number}'")
