while(1):
    try:
        n = int(input("Enter a number"))
        print(n)
    except Exception as e:
        print("unchecked exception")
