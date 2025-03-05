#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 04/03/2025
# It calculates the pizza cost


import constants


def main():
   # Get the input
   diameter = int(input("Enter diameter of pizza (cm): "))
   # Calculating the cost
   subtotal = constants.LABOUR_COST + \
       constants.RENTAL_COST + constants.INGRED_COST * diameter
   tax = constants.HST * diameter
   total = subtotal + tax
   # Display output
   print("The total cost is = ${:,.2f}".format(total))

if __name__ == "__main__":
    main()
