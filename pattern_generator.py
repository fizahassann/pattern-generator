print("====================================")
print("      Pattern Generator")
print("====================================")
print("1. Square Pattern")
print("2. Increasing Triangle")
print("3. Decreasing Triangle")
print("4. Exit")
while True: 
    print("Enter number of rows: ", end="")
    rows = int(input())
    print("Enter your choice: ", end="")
    choice = int(input())
    if choice == 1:
        for i in range(rows):
            for j in range(rows):
                print("*", end="")
            print()
    elif choice == 2:
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()
    elif choice == 3:
        for i in range(rows, 0, -1):
            for j in range(i):
                print("*", end="")
            print() 
    elif choice == 4:
        print("Thank you for using Pattern Generator")
        break
    else:
        print("Invalid choice. Please try again.")
    
