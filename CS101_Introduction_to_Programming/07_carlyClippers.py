hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# -- Calculate Price and Cuts --
# Sum all the prices of haircuts
total_price = 0
for price in prices:
  total_price += price
# Calculate the average price
average_price = total_price / len(prices)
# Print the price
print("Average Haircut Price: " + str(average_price))

# Create new price list
new_prices = [price - 5 for price in prices]
# Print new_prices
print(new_prices)

# -- Calculate Revenue --
total_revenue = 0
# Calculate total_revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))
# Average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)
# Haircuts under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]
print(cuts_under_30)