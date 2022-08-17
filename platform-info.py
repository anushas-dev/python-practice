import platform as pl

def platform_info():
    print("Sorry we couldn't answer your query but perhaps the below information might help")
    return 'OS', pl.system(), 'Arch', pl.machine(), 'Python', pl.python_version()

def ask_user_info(spec):
    if spec == 'OS':
        return pl.system()

    if spec == 'architecture':
        return pl.machine()

    elif spec == 'python':
        return pl.python_version()

    else:
        return platform_info()


print("Depending on your input we can show relevant info")
inp = input("Enter one of the words in [OS, architecture, python]: ")
print(ask_user_info(inp))
