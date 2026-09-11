from collections import deque

customer_products = deque()

def main():
    while True:
        print("\n--- Menu ---")
        print("Werehouse Program!")
        print("1.add products")
        print("2.view products")
        print("3.send products")
        print("4.cancel products")
        print("5.exit")

        choice = input("What do you want to do?: ").strip()
        if choice.isdigit() or choice == "" or not all(choice.isalpha() for choice in choice.replace(" ", "")):
            print("-> Please type your choice!")
            continue

#เพิ่ม product เข้าคลังสินค้า
        if choice == "add products":
                while True:
                    product = input("Enter your Product:").strip()
                    if product == "":
                        print("-> Product cannot be empty!")
                        continue

                    customer_products.append(product)
                    print(f"-> Added products!: {product}")
                    print(f"-> Current products in werehouse!: {len(customer_products)}")

                    while True: 
                        add_another = input("\nWould you like to add another product? (yes/no): ").strip().lower()
                        if add_another not in ("yes", "no"):
                            print("-> Please type yes or no!")
                            continue
                        break

                    if add_another == "no":
                        break
#ดูสินค้าที่อยู่ในคลังสินค้า

        elif choice == "view products":
                print(f"-> Current products in werehouse!: {len(customer_products)}")
                print(f"-> Name products in werehouse: {list(customer_products)}")

#ส่งสินค้าออกจากคลังสินค้า    
        elif choice == "send products":
            while True:
                if not customer_products:
                    print("-> Werehouse is empty!")
                    break
                    
                sent_product1 = customer_products.popleft()
                print(f"-> Sent products!: {sent_product1}")

                while True:
                    send_product1 = input("\nWould you like to send another product? (yes/no): ").strip().lower()
                    if send_product1 not in ("yes", "no") or send_product1 == "":
                        print("-> Please type yes or no!")
                        continue
                    break

                if send_product1 == "no":
                    break
                else:
                    print("-> Werehouse is empty!")

#ยกเลิกคำสั่งสินค้า

        elif choice == "cancel products":
            if customer_products:
                cancelled_product = customer_products.pop()
                print(f"-> Cancelled products!: {cancelled_product}")
            else:
                print("-> No products to cancel!")

#ออกจากโปรแกรมคลังสินค้า

        elif choice == "exit":
            print("-> Exiting...")
            break

        else:
            print("-> Invalid choice!")

if __name__ == "__main__":
    main()