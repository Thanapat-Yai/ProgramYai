from collections import deque

information = deque()

def main():
    while True:
        print("\n--- Menu ---")
        print("Welcome to the Queue Program!")
        print("1.add")
        print("2.pop")
        print("3.queue")
        print("4.exit")
        
        choice = input("type your choice (add pop queue exit): ").strip()
        
        if choice == "add":
            name = input("Enter your name: ").strip()
            if name == "":
                print("-> Name cannot be empty!")
                continue

            elif name.isdigit():
                print("-> Name cannot be a number!")
                continue

            item = input("Enter your menu: ").strip()
            if item == "":
                print("-> Menu cannot be empty!")
                continue

            elif item.isdigit():
                print("-> Menu cannot be a number!")
                continue
            else:
                information.append(item)
                print(f"-> Added menu!: {item} for {name}")
                print(f"-> Added Current queue!: {list(information)}")

        elif choice == "pop":
            if information: # ตรวจสอบก่อนว่ามีข้อมูลในคิวไหมเพื่อป้องกันข้อผิดพลาด
                removed = information.popleft()
                print(f"-> Called: {name}")
                print(f"-> Current queue: {list(information)}")
            else:
                print("-> Queue is empty!")
                
        elif choice == "queue":
            print(f"-> Current queue: {list(information)}")
            
        elif choice == "exit":
            print("thanks for using the Queue Program!")
            break
            
        else:
            print("please type your choice correctly (add pop queue exit)")

# เรียกใช้งานฟังก์ชันหลักข้างนอก Loop
if __name__ == "__main__":
    main()