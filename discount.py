
def calculate_discount(price, discount_percent):
    if discount_percent > 100 or discount_percent <= 0:
        print('Discount cannot be more than 100% or less than 0!!')
    else:
        if discount_percent>20:
            final_price = price - (price*(discount_percent/100))
            print(f"The final price is : {final_price}")
        else:
            print(f'Original price: {price}')
    return


user_price = int(input("Input the original price: "))
user_discount_percent = int(input('Enter the discount percent: '))

calculate_discount(user_price, user_discount_percent)
