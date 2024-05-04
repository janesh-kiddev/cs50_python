def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isnumeric():
        return False
    else:
        for i in s:
            if len(s)>=2 and len(s)<=6:
                if i.isalnum() or i.isalpha():
                    if i not in [',','?','.']:
                        if i.isdigit():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False

main()
