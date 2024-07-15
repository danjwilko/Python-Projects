# Modifying Global Scope

enemies = 1


# def increase_enemies():
# local variable
# enemies = 2
# global enemies
# enemies += 1
# print(f"enemies inside function: {enemies}")

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


increase_enemies()
# calling global variable
print(f"enemies outside function: {enemies}")

# avoid modifying global variables.
