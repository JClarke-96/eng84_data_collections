# Create a shopping list example
shopping_list = ["bread", "chocolate", "avacados", "milk"]

print(shopping_list)
print(type(shopping_list))
print(shopping_list[1])

shopping_list[2] = "orange" # Change index 2 (avacados) to orange
shopping_list.append("ice cream")  # Add a new item (ice cream) to list
shopping_list.remove("chocolate")   # Remove item (chocolate) from list
shopping_list.pop(-1)   # Remove last entry in list
print(shopping_list)