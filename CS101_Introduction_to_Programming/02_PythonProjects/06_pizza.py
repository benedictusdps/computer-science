# Track the kinds of pizza sold in the shop
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
# Track the prices of pizza sold in the shop
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of pizzas sold at $2
num_two_dollar_slices = prices.count(2)
# Count the number of toppings available
num_pizzas = len(toppings)
# Print the number of pizzas sold in the shop
print(f"We sell {num_pizzas} different kinds of pizza!")

# Combine the pizzas and prices list
pizzas_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]
# Print the pizzas and prices list
print(pizzas_and_prices)

# Sort ascending based on price
pizzas_and_prices.sort()
# Check for cheapest pizza
cheapest_pizza = pizzas_and_prices[0]
# Check for most expensive pizza
priciest_pizza = pizzas_and_prices[-1]
# Remove the most expensive pizza
pizzas_and_prices.pop()
# Add new topping
pizzas_and_prices.insert(4, [2.5, "pepper"])

# Get the 3 cheapest pizza
three_cheapest = pizzas_and_prices[:3]
print(three_cheapest)
