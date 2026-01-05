# # YOUR CODE HERE
# n = int(input()) #รับค่า n จำนวนใน list
# lst1 = [] #สร้าง list1
# lst2 = [] #สร้าง list2

# for i in range(n): #ลูป n ครั้ง
#     while i != n: #ลูป
#         x = int(input()) #ใส่ตัวเลข
#         lst1.append(x) #เพิ่มค่า x ลงใน lst1
#         break
# for i in range(n): #ลูป n ครั้ง
#     y = int(input()) #ใส่ตัวเลข
#     lst2.append(y) #เพิ่มค่า y ลงใน lst2

# def summation(lst1, lst2): #function summation รับ lst1, lst2
#     updated_list = [lst1[i] + lst2[i] for i in range(len(lst1))] #updated_list คือ lst1 + lst2 โดยที่ i เป็น len (จำนวน) ใน lst
#     return updated_list #return ค่า updated_list

# def find_min_max(lst): #หา min_max
#     return min(lst), max(lst) #return ค่า min และค่า max

# updated_list = summation(lst1, lst2) #updated_list = ค่า summation lst ที่บวกกัน
# print(updated_list) #print updated_list

# min, max = find_min_max(updated_list) #min, max = ค่า min_max ของ updated_list
# print((min, max)) #print (min,max)
