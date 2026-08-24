import random
THRESHOLD = 50

def read_sensor():
    # จำลองค่าฝุ่น (ยังไม่มีเซนเซอร์จริง)
    value = random.randint(10, 120)
    print("ค่าฝุ่น PM2.5:", value)
    return value
 
def main():
    print("Start")
 
    # อ่านค่าฝุ่น
    pm25 = read_sensor()
 
    # เช็คว่าเกินเกณฑ์ไหม
    if pm25 > THRESHOLD:
        print("Red LED: แจ้งเตือน")
    else:
        print("Green LED: ปกติ")
 
    # เลือกโหมด
    mode = input("เลือกโหมด (1=Auto, 2=Manual): ")
 
    if mode == "1":
        # Auto: เช็คซ้ำแล้วตัดสินใจพ่นน้ำเอง
        if pm25 > THRESHOLD:
            print("พ่นน้ำ + เปิดพัดลม")
        else:
            print("ไม่ต้องพ่นน้ำ")
    else:
        # Manual: รอผู้ใช้กดปุ่ม
        input("กด Enter เพื่อสั่งพ่นน้ำ...")
        print("พ่นน้ำ + เปิดพัดลม")
 
    # อัปเดต LED
    print("Update LED:", pm25)
    print("End")
 
if __name__ == "__main__":
    main()