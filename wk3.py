# Define a function named calculate_discount
def calculate_discount(price, discount_percent):
    """
    This function calculates the final price after applying a discount.
    If the discount is 20% or higher, it applies the discount.
    Otherwise, it returns the original price.
    """
    # Check if the discount percentage is 20 or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate and return the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price


# Prompt the user to enter the original price
original_price = float(input("Enter the original price of the item: "))

# Prompt the user to enter the discount percentage
discount_percentage = float(input("Enter the discount percentage: "))

# Call the calculate_discount function to get the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price or the original price
if final_price != original_price:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount was applied. The original price is: {original_price}")