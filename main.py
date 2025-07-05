from utils import greet_user
from processor import process_items

def run_app():
    user = input("Enter your name: ")
    greet_user(user)

    items = ["apple", "banana", "cherry"]
    result = process_items(items)
    print("Processed items:", result)

if __name__ == "__main__":
    run_app()