from collections import Counter

grocery_list = []

while True:
    try:
        item = input().strip().lower()
        grocery_list.append(item)
    except EOFError:
        break

item_counts = Counter(grocery_list)

sorted_items = sorted(item_counts.keys())

print("Grocery List:")
for item in sorted_items:
    count = item_counts[item]
    print(f"{count} {item.upper()}")