from collections import OrderedDict

items_count = int(input())
ordered_dictionary = OrderedDict()
for i in range(items_count):
    item_name, item_count = input().rsplit(" ",1)
    if item_name in ordered_dictionary:
        ordered_dictionary[item_name] = int(ordered_dictionary[item_name]) + int(item_count)
    else:
        ordered_dictionary[item_name] = int(item_count)

for item, count in ordered_dictionary.items():
    print(f"{item} {count}")
