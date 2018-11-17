def grand_c_d(a, b):
    r = 1
    x = a
    y = b
    while r != 0:
        r = a % b
        if r != 0:
            a = b
            b = r
    print(f"GCD({x},{y})={b}")

def process(a,b):
    if a == 0 and b != 0:
        print(f"GCD({a},{b})={b}")
    elif a != 0 and b == 0:
        print(f"GCD({a},{b})={a}")
    elif a == 0 and b == 0:
        print("GDC(0,0)= none")
    elif a >= b:
        grand_c_d(a, b)
    else:
        grand_c_d(b, a)

def main():
    a = input("enter first integer:")
    while a != "q":
        a = int(a)
        b = int(input("enter second integer"))
        process(a, b)
        a = input("enter an integer or(q) to quit  :")

if __name__=="__main__":
    main()


#enter first integer:>? 123
#enter second integer>? 12
#GCD(123,12)=3

#enter first integer:>? 120
#enter second integer>? 12
#GCD(120,12)=12

#enter first integer:>? 0
#enter second integer>? 34
#GCD(0,34)=34
