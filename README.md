ip = input("Enter IP address: ")

try:
    parts = ip.split('.')
    first = int(parts[0])
    second = int(parts[1])

    if first == 10:
        print("Private IP")
        print("Type: Class A Private")
        print("Use: Large company network")

    elif first == 172:
        if second >= 16 and second <= 31:
            print("Private IP")
            print("Type: Class B Private")
            print("Use: Medium company network")
        else:
            print("Public IP")
            print("Use: Internet")

    elif first == 192 and second == 168:
        print("Private IP")
        print("Type: Class C Private")
        print("Use: Home or small office network")

    elif first == 127:
        print("Loopback IP")
        print("Use: Your own computer")

    else:
        print("Public IP")
        print("Use: Internet")

except:
    print("Invalid IP format. Example: 192.168.1.1")
