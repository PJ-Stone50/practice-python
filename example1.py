# 1.ร้านขายหนังสือร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ ถ้าคุณซื้อหนังสือมากกว่า 3 เล่ม ที่มีมูลค่ารวมเกิน 500 บาท คุณจะได้ส่วนลด 10%

# ให้เขียนโปรแกรมรับจำนวนหนังสือที่ซื้อและราคารวม จากนั้นคำนวณราคาที่ต้องจ่าย

# Sample output1

# How many books: 2
# How much: 1000
# You have to pay 1000 bath.

# Sample output2

# How many books: 5
# How much: 500
# You have to pay 500 bath.

# Sample output3

# How many books: 5
# How much: 600
# You have to pay 540 bath.
# *********************************************************

book_count = int(input("How many books: "))
book_price = int(input("How much: "))
book_total = 0
if book_count > 3 and book_price > 500:
    book_total = book_price * 9/10
else:
    book_total = book_price
    

print("You have to pay %d"%book_total)