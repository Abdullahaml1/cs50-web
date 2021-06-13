def login(f):
    def wrapperFunction():
        print("We are processing the data of the input user")
        f()
        print("fuction was applied")

    return wrapperFunction


@login
def hello():
    print("hello")


hello()


