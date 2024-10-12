# The Lists
# Use [...] to create a list - Var = []
minecraft_mobs = ["creeper", "Skeleton", "Spider", "Zombie"]

# Manipulation
minecraft_mobs[1] = "Tengkorak"
# .append() - Add item to the list
minecraft_mobs.append("Pillager")
# .extend([]) - Add another list of items to the list
minecraft_mobs.extend(["Evoker", "Vindicator", "Ravager"])
# .insert() - Insert item to specified position
minecraft_mobs.insert(0, "Enderman")
# .remove() - Remove an item from the list
minecraft_mobs.remove("Spider")

print(minecraft_mobs)
print(minecraft_mobs[1])
