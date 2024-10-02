# Example 1
print("Example 1")

def stock_status_decorator(func):
    def wrapper(item):
        result = func(item)
        print(result, ": stock status for", item)
        return result

    return wrapper


@stock_status_decorator
def restock_item(item):
    return "Restocked"


@stock_status_decorator
def sell_item(item):
    return "Sold"


print(restock_item("Laptop"))
print(sell_item(" Smartphone"))


# Example 2
print("\nExample 2")

import time


def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Function took:", time.time() - before, "seconds")

    return wrapper


@timer
def run():
    time.sleep(3)
    
run()
