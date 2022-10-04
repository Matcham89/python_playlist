

print("Please enter the weightof your package...")
weight = input()

#flat rates
ground_shipping = 20
premium_shipping = 125
drone_shipping = 0

#ground shipping price per pound
cost_1 = int(weight)*1.50
cost_2 = int(weight)*3.00
cost_3 = int(weight)*4.00
cost_4 = int(weight)*4.75

#drone shipping price per pound
cost_5 = int(weight)*4.50
cost_6 = int(weight)*9.00
cost_7 = int(weight)*12.00
cost_8 = int(weight)*14.25

#ground shipping flat rate + price per pound
option_1 = int(ground_shipping) + int(cost_1)
option_2 = int(ground_shipping) + int(cost_2)
option_3 = int(ground_shipping) + int(cost_3)
option_4 = int(ground_shipping) + int(cost_4)

#drone flat rate + price per pound
option_5 = int(drone_shipping) + int(cost_5)
option_6 = int(drone_shipping) + int(cost_6)
option_7 = int(drone_shipping) + int(cost_7)
option_8 = int(drone_shipping) + int(cost_8)

print("Ground Shippint")
print("under 2lb £" + str(option_1)) 
print("Over 2 lb but less than or equal to 6 lb £" + str(option_2))
print( "Over 6 lb but less than or equal to 10 lb £" + str(option_3))
print("Over 10 lb £" + str(option_4)) 
print(" ")
print("Drone Shipping")
print("under 2lb £" + str(option_5))
print("Over 2 lb but less than or equal to 6 lb £" + str(option_6)) 
print("Over 6 lb but less than or equal to 10 lb £" + str(option_7)) 
print("Over 10 lb £" + str(option_8))
print(" ")
print("Given the weight of your package at " + str(weight) + "lb")

option = "The cheapest option for shipment is "
grnd = "*Ground Shipping* "
prem = "*Premium Shipping* "
drone = "*Drone Shipping* "
if option_1 > option_5 and int(weight) <= 2 and option_1 < premium_shipping:
    print(option + drone + "at the cost of £" + str(option_5) + " option 5")
elif option_1 > option_5 and int(weight) <= 2 and option_1 > premium_shipping:
    print(option + prem + "at the cost of £" + str(premium_shipping) + " premium shipping")

elif option_2 > option_6 and int(weight) <= 6 and option_2 < premium_shipping:
    print(option + drone + "at the cost of £" + str(option_6) + " option 6")
elif option_2 > option_6 and int(weight) <= 6 and option_2 > premium_shipping:
    print(option + prem + "at the cost of £" + str(premium_shipping) + " premium shipping")

elif option_3 > option_7 and int(weight) <= 10 and option_3 < premium_shipping:
    print(option + drone + "at the cost of £" + str(option_7) + " option 7")
elif option_3 > option_7 and int(weight) <= 10 and option_2 > premium_shipping:
    print(option + prem + "at the cost of £" + str(premium_shipping) + " premium shipping")

elif option_4 > option_8 and int(weight) > 10 and option_4 < premium_shipping:
    print(option + drone + ", at the cost of £" + str(option_8) + " option 8")
elif option_4 > option_8 and int(weight) > 10 and option_4 > premium_shipping:
    print(option + prem + "at the cost of £" + str(premium_shipping) + " premium shipping")

elif option_5 > option_1 and int(weight) <= 2 and option_5 < premium_shipping:
    print(option + grnd + "at the cost of £" + str(option_1) + " option 1")
elif option_5 > option_1 and int(weight) <= 2 and option_5 > premium_shipping:
    print(option + prem + "at the cost of £" + str(premium_shipping) + " premium shipping")

elif option_6 > option_2 and int(weight) <= 6 and option_6 < premium_shipping:
    print(option + grnd + "at the cost of £" + str(option_2) + " option 2")
elif option_6 > option_2 and int(weight) <= 6 and option_6 > premium_shipping:
    print(option + prem + "at the cost of £" + str(premium_shipping) + " premium shipping")

elif option_7 > option_3 and int(weight) <= 10 and option_7 < premium_shipping:
    print(option + grnd + "at the cost of £" + str(option_3) + " option 3")
elif option_7 > option_3 and int(weight) <= 10 and option_7 > premium_shipping:
    print(option + prem + "at the cost of £" + str(premium_shipping) + " premium shipping")

elif option_8 > option_4 and int(weight) > 10 and option_8 < premium_shipping:
    print(option + grnd + "at the cost of £" + str(option_4) + " option 4")
elif option_8 > option_4 and int(weight) > 10 and option_7 > premium_shipping:
    print(option + prem + "at the cost of £" + str(premium_shipping) + " premium shipping")

