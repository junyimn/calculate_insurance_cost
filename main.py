# Create calculate_insurance_cost() function below:

def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    return print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
    return estimated_cost


# Initial variables for Maria


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)

# Initial variables for Omar
age = 35
sex = 1
bmi = 22.2
num_of_children = 0
smoker = 1

# Estimate Omar's insurance cost

omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)

# My insurance cost

michael_insurance_cost = calculate_insurance_cost("Michael", 26, 1, 29.7, 0, 0)


# Create a second function to calculate the difference between the insurance costs (given as inputs) of any two individuals and print a statement saying: "The difference in insurance cost is xxx dollars."

# def calculate_difference(person1, person2):
#   if person1 > person2:
#     return person1 - person2
#   else:
#     return person2 - person1

# print(calculate_difference(10,4))


def calculate_difference(person1, person2):
    x = person1 - person2 if person1 > person2 else person2 - personn
    print("The difference in insurance cost is " + str(x) + " dollars.")


calculate_difference(324234, 24334)

