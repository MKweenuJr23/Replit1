def add_item_to_list():
    item = input("Enter an item to add to your shopping list: ")
    shopping_list.append(item)

shopping_list = []
for _ in range(5):
    add_item_to_list()

print("\nYour shopping list:")
for item in shopping_list:
    print(f"- {item}")