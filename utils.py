def greet_user(name):
    """
    Simple greeting utility.
    """
    if not name:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name.title()}!")