# #conditions
#
# # a = int(input('Enter a value for a: '))
# # b = int(input("Enter a value for b: "))
# # c = int(input("Enter a value for c: "))
# # d = int(input("Enter a value for d: "))
# # if a >= b and a >= c and a >= d:
# #     print('a is greater')
# # elif b >= a and b >= c and b >= d:
# #     print('b is greater')
# # elif c >= a and c >= b and c >=d :
# #     print("c is greater")
# # else:
# #     print("d is greater.")
#
#
# # # WAP to input the age of a person and decide if he is allowed to enter the club or not.
# #
# # userAge = int(input("Enter your age: "))
# # if userAge < 18:
# #     print("Your below the age limit, you're restricted.")
# # elif userAge >=18 and userAge <= 40:
# #     print("Welcome to the club.")
# # else:
# #     print("You must be over 40 , you're over-aged.")
#
# # WAP to input nep, eng, math, scie,
# # 35-45 -3rd
# # 45- 60
# # 60 - 80
# # 80 - 100 distinction
#
#
# nepali = int(input("Enter your marks of nepali : "))
# english = int(input("Enter your marks of eng: "))
# science = int(input("Enter your marks of science: "))
# maths = int(input("Enter your makrs for maths "))
#
# total = nepali + english + science + maths
# percentage = total * 100/400
#
# if percentage < 35:
#     print('FAIL, you scored below ', + percentage)
# elif percentage >= 35 and percentage <= 45:
#     print("You're third!, you scored ", + percentage)
# elif percentage >= 45 and percentage <= 60:
#     print("You're second!, you scored ", + percentage)
# elif percentage >= 60 and percentage <= 80:
#     print("You're first!, you scored ", + percentage )
# else:
#     print("You scored distinction, excellent!", + percentage)

#computer bazaar
# dell 20k
# toshiba 30k
# macbook 50k
# select product by typing 1,2 or 3
# select quantity and display total price number of products * price
# delivery option
# home = 1000
# pickup = (free)
# packing: 1) plastic bag= 500 1) bag 100    3) gift box = 5000
# location: 1)ktm = 13% tax in price of product only.    2) lalitpur = 14%  3) bhaktapur = 15%

# install git = scm
# create bithub account

print("""
Welcome to Computer bazaar portal!.
our products are:
1) Dell = Rs 20,000
2) Toshiba = Rs30,000
3) macbook = rs 50,000
__________________________________________________
Press the allocated numbers to choose the product.
1) Dell 
2) Toshiba 
3) macbook
""")
dell = 20000
toshiba = 30000
macbook = 50000
total = 0
units = 0
plastic_bag = 20
jute_bag = 50
gift_box = 100
address = ""
product_input = input("Enter the allocated number of the product you want to choose: ".lower())
if product_input == "1" or product_input == "dell":
    print("Dell laptop has been added to your cart. ")
    total += dell
elif product_input == "2" or product_input == 'toshiba':
    print("Toshiba laptop has been added to your cart.")
    total += toshiba
elif product_input == "3" or product_input == "macbook":
    print("Macbook has been added to your cart.")
    total += macbook
else:
    print("INVALID")

# Taking input of number of units of the product
units = int(input("Now please input the number of units you'd like to purchase: "))
total = units * total

# Taking input of delivery option.
print("""
Please choose your desired option to receive the product: 
1) Delivery (KTM = Rs100/ LTP = Rs300 / BKP = Rs500)
2) Pick-up
""")
receive = int(input("Choose between the two (1/2): "))
if receive == 2:
    print("""
    How'd you like your product/products packaged?
    1) Plastic bag: Rs20
    2) Jute bag   : Rs50
    3) Gift box   : Rs100
    """)
    packaging = int(input("Choose between the three (1/2/3): "))
    if packaging == 1:
        print("Plastic bag has been added to your cart.")
        total += plastic_bag
    elif packaging == 2:
        print("Jute bag has been added your cart.")
        total += jute_bag
    elif packaging == 3:
        print("Gift box has been added to your cart.")
        total += gift_box
    else:
        print("INVALID")
elif receive == 1:
    print("""
    Delivery locations:
    1) Kathmandu
    2) Lalitpur
    3) Bhaktapur
    """)
    address = int(input("Please choose your location(1/2/3):  "))
    if address == 1:
        print("Rs 100 delivery charge has been added.")
        total += 100
    elif address == 2:
        print("Rs 300 delivery charge has been added.")
        total += 300
    elif address == 3:
        print("Rs 500 delivery charge  has been added.")
        total += 500
    else:
        print("INVALID!")
    print("""
        How'd you like your product/products packaged?
        1) Plastic bag: Rs20
        2) Jute bag   : Rs50
        3) Gift box   : Rs100
        """)
packaging = int(input("Choose between the three (1/2/3): "))
if packaging == 1:
    print("Plastic bag has been added to your cart.")
    total += plastic_bag
elif packaging == 2:
    print("Jute bag has been added your cart.")
    total += jute_bag
elif packaging == 3:
    print("Gift box has been added to your cart.")
    total += gift_box
else:
    print("INVALID")
tax = total*13/100
total += tax


print("""
Thank you for choosing Computer Bazaar!
Your total bill along with added tax is Rs""", + total)












