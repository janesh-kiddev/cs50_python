def main(grt):
    if grt[0].startswith("hello"):
        print("$0")
    elif grt[0].startswith("how"):
        print("$20")
    else:
        print("$100")


ask = input("Greeting:").lower().split()
main(ask)
