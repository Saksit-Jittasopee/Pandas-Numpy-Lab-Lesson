# YOUR CODE HERE
'''
Example of Function Uses:
cal_dist(x1,y1,z1,x2,y2,z2) 
'''
import math #import math เพื่อใช้ในการคำนวณหา square root และยกกำลัง

def cal_dist(x1=7.0, y1=4.0, z1=3.0, x2=17.0, y2=6.0, z2=2.0): #สร้าง function cal_dist และกำหนด default parameter
    dist = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2) + math.pow((z1 - z2), 2)) #คำนวณหาค่า dist (ระยะทาง 3 มิติ)
    return round(dist, 2) #return ค่า dist เป็นทศนิยม 2 ตำแหน่ง

def input_dist(): #สร้าง function input_dist เพื่อสำหรับเก็บค่า input
        x1 = input() #input ค่า x1
        y1 = input() #input ค่า y1
        z1 = input() #input ค่า z1
        x2 = input() #input ค่า x2
        y2 = input() #input ค่า y2
        z2 = input() #input ค่า z2

        if x1 == 'q' or y1 == 'q' or z1 == 'q': #ถ้า x1,y1 หรือ z1 == q 
            x1, y1, z1 = 7.0, 4.0, 3.0 #ให้นำ default parameter ของแต่ละค่ามาแทน
        else: #ถ้า x1,y1 หรือ z1 ไม่ใช่ q 
            x1, y1, z1 = float(x1), float(y1), float(z1) #ให้แปลงค่า input จาก str เป็น float 

        if x2 == 'q' or y2 == 'q' or z2 == 'q': #ถ้า x2,y2 หรือ z2 == q 
            x2, y2, z2 = 17.0, 6.0, 2.0 #ให้นำ default parameter ของแต่ละค่ามาแทน
        else: #ถ้า x2,y2 หรือ z2 ไม่ใช่ q 
            x2, y2, z2 = float(x2), float(y2), float(z2) #ให้แปลงค่า input จาก str เป็น float 

        distance = cal_dist(x1, y1, z1, x2, y2, z2) #distance คือค่า x1, y1, z1, x2, y2, z2
        print(distance) #print distance
input_dist() #แสดงค่า input_dist()