fruit_shop = {
    "kiwi": 20,
    "gauva": 35,
    "apple": 10,
    "mango": 8
}

key_to_check = input("What are you looking for? ").lower()

if(key_to_check in fruit_shop):
    print("Yes, this is available")
else:
    print("No, this is not available")