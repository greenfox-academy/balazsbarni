shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list. 
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)

for i in shop_items:
    if i == 2:
        shop_items[1] = "Croissant"
    elif i == False:
        shop_items[3] = "Ice Cream"
print(shop_items)