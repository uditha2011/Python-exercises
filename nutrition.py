# Given table of fruits and calories
table = [
    ["Fruit", "Calories"],
    ["Apple", "130"],
    ["Avocado", "50"],
    ["Banana", "110"],
    ["Cantaloupe", "50"],
    ["Grapefruit", "60"],
    ["Grapes", "90"],
    ["Honeydew Melon", "50"],
    ["Kiwifruit", "90"],
    ["Lemon", "15"],
    ["Lime", "20"],
    ["Nectarine", "60"],
    ["Orange", "80"],
    ["Peach", "60"],
    ["Pear", "100"],
    ["Pineapple", "50"],
    ["Plums", "70"],
    ["Strawberries", "50"],
    ["Sweet Cherries", "100"],
    ["Tangerine", "50"],
    ["Watermelon", "80"]
]

# Get user input for the fruit they want to check
fruit_name = input("Item: ")

# Initialize a variable to store the calorie value
calories = None

# Search for the fruit in the table and retrieve its calories
for row in table:
    if row[0].lower() == fruit_name.lower():
        calories = row[1]
        print(f"Calories: {calories}")
        break

# Check if the fruit was found and print the calories
# if calories is not None:
    # print(f"Calories: {calories}")
# else:
#     continue
