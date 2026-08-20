import sys

# Define the baseline year and list of zodiac signs starting from 1900 (Rat)
BASELINE_YEAR = 1900
ZODIAC_SIGNS = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

# a. Ask the user to enter a year of birth
try:
    birth_year = int(input("Enter your birth year: "))
except ValueError:
    print("Invalid Input, please enter a valid year number.")
    sys.exit()

# b. Validate user input that it should not be earlier than 1900
if birth_year < BASELINE_YEAR:
    # c. Display error message and stop/abort the program
    print("Invalid Year, it should not be earlier than 1900")
    sys.exit()

# d. Determine the Chinese zodiac sign using modulo arithmetic
zodiac_index = (birth_year - BASELINE_YEAR) % 12
zodiac_sign = ZODIAC_SIGNS[zodiac_index]

# Output the result matching the required format
print(f"Your Chinese Zodiac Sign is: {zodiac_sign}")
