# Day-3 - Feb 17 - Task 1
smith_age: int = 45
john_age: int = 45
henry_age: int = 45
name1 = "smith"
name2 = "john"
name3 = "henry"
if smith_age > john_age > henry_age:
    print("Henry is youngest")
    print(50 * "-")

elif henry_age > smith_age > john_age:
    print("john is youngest")
    print(50 * "-")

elif john_age > henry_age > smith_age:
    print("smith is youngest")
    print(50 * "-")

elif henry_age > john_age > smith_age:
    print("smith is youngest")
    print(50 * "-")

elif john_age > smith_age > henry_age:
    print("henry is youngest")
    print(50 * "-")

else:
    print(name1, name2, name3, "are of same age")
    print(50 * "-")

# Task - 2 - Part 1
cust_name = "Mary Smith"
message = " wants to purchase "
item_desc = "Shirt"
print(cust_name + message + item_desc)
print(50 * "-")

# Task - 2 - Part 2
price: float = 10
tax: float = 2
quantity: int = 3
total = price * quantity * tax

print(str(cust_name + message + str(quantity) + " " + item_desc))
print(50 * "-")
print("Total cost with tax is", str(total))
print(50 * "-")

# Task - 2 - Part 3
out_of_stock: bool = False
if quantity > 1:
    multi = item_desc + "s"
    print(str(cust_name + message + str(quantity) + " " + multi))
    print(50 * "-")

if out_of_stock:
    print("Items are not available")
    print(50 * "-")
elif not out_of_stock:
    print(message, "Total cost with tax is", str(total))
    print(50 * "-")

# Task - 2 - Part 4
a_list = ["shirt", "tshirt", "jeans", "shorts"]
list_len = len(a_list)
print(str(cust_name + message + str(len(a_list)) + " " + item_desc))