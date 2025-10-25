# patterns.py

def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def triangle(n):
    for i in range(1, n+1):
        print("* " * i)

def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# 🛠️ Main program
print("Choose a pattern:")
print("1. Square\n2. Triangle\n3. Inverted Triangle\n4. Pyramid\n5. Hollow Square")
choice = input("Enter pattern number (1-5): ")
size = int(input("Enter size: "))

print("\n🎨 Here's your pattern:\n")

if choice == "1":
    square(size)
elif choice == "2":
    triangle(size)
elif choice == "3":
    inverted_triangle(size)
elif choice == "4":
    pyramid(size)
elif choice == "5":
    hollow_square(size)
else:
    print("❌ Invalid choice.")
