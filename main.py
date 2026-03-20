import math

class Calc:
    def __init__(cal):
        cal.his = []

    def dis_menu(cal):
        print("\n===== SMART CALCULATOR =====")
        print("1. Basic Calculation")
        print("2. Scientific Functions")
        print("3. Extra Functions")
        print("4. Show History")
        print("5. Exit")

    def basic(cal):
        try:
            exp = input("Enter expression (e.g. 2 + 3 * 4): ")
            ans = eval(exp)
            print("Result:", ans)
            cal.his.append(f"{exp} = {ans}")
        except:
            print("Invalid Expression")

    def sci(cal):
        print("\n--- Scientific ---")
        print("1. sin")
        print("2. cos")
        print("3. log")
        print("4. sqrt")

        ch = input("Choose option: ")

        try:
            x = float(input("Enter number: "))

            if ch == '1':
                ans = math.sin(x)
                name = "sin"
            elif ch == '2':
                ans = math.cos(x)
                name = "cos"
            elif ch == '3':
                ans = math.log(x)
                name = "log"
            elif ch == '4':
                ans = math.sqrt(x)
                name = "sqrt"
            else:
                print("Invalid choice")
                return

            print("Result:", ans)
            cal.his.append(f"{name}({x}) = {ans}")

        except:
            print("Invalid Input")

    def extra(cal):
        print("\n--- Extra Functions ---")
        print("1. Power (x^y)")
        print("2. Factorial (x!)")
        print("3. Percentage")

        ch = input("Choose option: ")

        try:
            if ch == '1':
                x = float(input("Enter base (x): "))
                y = float(input("Enter power (y): "))
                ans = x ** y
                print("Result:", ans)
                cal.his.append(f"{x}^{y} = {ans}")

            elif ch == '2':
                x = int(input("Enter number: "))
                ans = math.factorial(x)
                print("Result:", ans)
                cal.his.append(f"{x}! = {ans}")

            elif ch == '3':
                x = float(input("Enter number: "))
                ans = x / 100
                print("Result:", ans)
                cal.his.append(f"{x}% = {ans}")

            else:
                print("Invalid choice")

        except:
            print("Invalid Input")

    def show(cal):
        print("\n--- History ---")
        if not cal.his:
            print("No calculations yet")
        else:
            for i in cal.his:
                print(i)

    def run(cal):
        while True:
            cal.dis_menu()
            ch = input("Enter choice: ")

            if ch == '1':
                cal.basic()
            elif ch == '2':
                cal.sci()
            elif ch == '3':
                cal.extra()
            elif ch == '4':
                cal.show()
            elif ch == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again")


c = Calc()
c.run()
