
class SalaryError(ValueError):
    pass


# Python exception hierachy
while True:
    try:
        _input = input("Please input salary: ")
        if _input == "exit":
            break
        elif not _input.isdigit():
            raise SalaryError("Invalid salary type")
        else:
            salary = int(_input)
        print(salary)
    except SalaryError as e:
        print("Invalid salary amount, plase try again or print exit to stop")