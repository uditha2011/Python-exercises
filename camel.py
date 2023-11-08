def camel_to_snake(camel_name):
    snake_name = ""
    for text in camel_name:
        if text.isupper():
            snake_name += "_" + text.lower()
        else:
            snake_name += text
    return snake_name.lstrip("_")

def main():
    camel_name = input("camelCase: ")
    snake_name = camel_to_snake(camel_name)
    print(f"snake_case: {snake_name}")

# if __name__ == "__main__":
main()

# i=2
# x = int(i)
# while i < 20:
#     x /= 2
#     print(x)
#     i += 1
