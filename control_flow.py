# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':


letter = input("Please enter a letter: ")
vowels = 'aeiou'

if letter in vowels:
    print(f"The Letter {letter} is a vowel")
else:
    print(f"The letter {letter} is a consonant")

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = input("Please enter a phrase: ")
def phrase_length(phrase):
    counter = 0
    for char in phrase:
        counter += 1
    print(f"What you entered is {counter} characters long")
print(f"What you entered is {len(phrase)} characters long")
phrase_length(phrase)

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age:
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
dog_age = int(input("Input a dog's age: "))

def count_dog_years(dog_years):
        counter = 0
        sum = 0
        for years in range(dog_years):
            counter += 1
            if counter <= 2:
                sum += 10
            elif counter > 2:
                sum += 7
        print(f"The dog's age in dog years is {sum}")

count_dog_years(dog_age)



# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

a_side = int(input("Please enter length of a: "))
b_side = int(input("Please enter length of b: "))
c_side = int(input("Please enter length of c: "))

def check_triangle(a,b,c):
    if a == b and b == c:
        print("equilateral - all three sides are equal in length")
    elif a == b or b == c or c == a:
        print("isosceles - exactly two sides are the same length")
    elif a != b or b != c or c != a:
        print("scalene - all three sides are unequal in length")

check_triangle(a_side,b_side,c_side)


# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

fibonacci_sequence = [0, 1]

for n in range(2, 50):
    next_number = fibonacci_sequence[n - 1] + fibonacci_sequence[n - 2]
    fibonacci_sequence.append(next_number)

for term, number in enumerate(fibonacci_sequence):
    print(f"term: {term} / number: {number}")




# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>


month = input("Enter the month of the year (Jan - Dec): ").lower()
day = int(input("Enter the day of the month: "))

def check_season(month, day):
    spring_season = ('mar', 'apr', 'may', 'jun')
    summer_season = ('jun', 'jul', 'aug', 'sep')
    fall_season = ('sep', 'oct', 'nov', 'dec')
    winter_season = ('dec', 'jan', 'feb', 'mar')

    season = None

    # Check for spring
    if month in spring_season:
        season = 'spring'
    if month == 'mar' and day >= 20:
        season = 'spring'
    if month == 'jun' and day <= 20:
        season = 'spring'

    # Check for summer
    if month in summer_season:
        season = 'summer'
    if month == 'jun' and day >= 21:
        season = 'summer'
    if month == 'sep' and day <= 21:
        season = 'summer'

    # Check for fall
    if month in fall_season:
        season = 'fall'
    if month == 'sep' and day >= 22:
        season = 'fall'
    if month == 'dec' and day <= 20:
        season = 'fall'

    # Check for winter
    if month in winter_season:
        season = 'winter'
    if month == 'dec' and day >= 21:
        season = 'winter'
    if month == 'mar' and day <= 19:
        season = 'winter'

    return season

season = check_season(month, day)

print(f"{month.capitalize()} {day} is in {season}")
