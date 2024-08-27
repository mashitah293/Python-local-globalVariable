counter = 0

def increment_counter():
    global counter  
    counter += 1  
    print(f"Global counter after increment: {counter}")

def reset_counter():
    counter = 0  
    print(f"Local counter after reset: {counter}")

increment_counter()
print(f"Global counter: {counter}")

increment_counter()
print(f"Global counter: {counter}")

increment_counter()
print(f"Global counter: {counter}")

reset_counter()
print(f"Global counter: {counter}")



