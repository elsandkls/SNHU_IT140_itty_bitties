# Rental Car Project 
import sys

#define cars available for rental:
cars = ["",
"Mitsubishi Mirage, 4P/2B, REN-5601, 12678, Red, 25, 9.99",
"Nissan Versa, 5P/1B, REN-5824, 56753, Blue, 50, 9.99",
"Hyundai Elantra, 5P/1B, REN-3541, 23456, Black, 75, 9.99",
"Kia Soul, 5P/2B, REN-3548, 29412, White, 100, 9.99",
"Toyota Camry, 5P/2B, REN-3974, 23673, Yellow, 50, 15.99",
"Nissan Maxima, 5P/4B, REN-3675, 12357, Green, 75, 15.99",
"Chevrolet Impala, 5P/4B, REN-1588, 98723, Purple, 100, 15.99",
"Cadillac XTS, 5P/2B, REN-3624, 21556, Orange, 25, 15.99",
"Ford Mustang, 4P/2G, REN-6549, 23136, Pink, 75, 23.99",
"Mercedes Benz CLA, 5P/1B, REN-3648, 12347, Red, 50, 23.99",
"Infiniti Q50, 5P/2B, REN-3124, 34578, Blue, 100, 23.99",
"Audi A6, 5P/3B, REN-3647, 23456, Black, 25, 23.99",
"Toyota Prius, 5P/2B, REN-9187, 32403, Yellow, 75, 35.99",
"Ford Fusion Hybrid, 5P/2B, REN-9815, 39872, White, 100, 35.99",
"Dodge Challenger, 4P/2B, REN-3128, 12521, Green, 25, 45.99",
"Nissan LEAF, 5P/1B, REN-4978, 23678, Purple, 50, 55.99"]

#define the start and stop points for looping through the array
car_start = int(0)
car_stop = len(cars)
car_myinc = int(1)

# menu for a simple rental car billing calculator. 
menu_main = [ "   ",
"####################################",
"###  Rental Car Billing Script   ###",
"####################################",
"  1. List available cars. ",
"  2. Select a car for rental. ",
"  3. Enter the customers information. ",
"  4. Print Receipt. ",
"  5. ",
"  6. Exit program. ",
" ",
" "]

# reciept page
receipt_page = ["",
" ",        
"####################################",
"###  Rental Car Customer Receipt ###",
"####################################",
" ",
" Customer Name:",
" Car Selected: ",
" Color: ",
" Milage: ",
" Fuel Out: ",
" Liscense: ",
" Unit: ",
" ###################################",
" ",
" Car Daily Rate: ",
" Damage Waiver: ",
" Car Ins Daily Rate: ",
" Tax Percentage: ",
" ###################################",
" ",
" Additional Mileage: ",
" Excess Distance: ",
" Refueling Charge: ",
" Daily Milage: ",
" ###################################",
" ",
" Pickup Date: ",
" Pickup Time: ",
" Drop Off Date: ",
" Drop Off Time: ",
" ###################################",
" ",
" Sub Total: ",
" Sales Tax: ",
" Total: ",
" ###################################",
""]

#define the start and stop points for looping through the array
menu_start = int(0)
menu_stop = len(menu_main)
menu_myinc = int(1)
menu_selection = int(0)

# string for receipt printing
print_me = " "
pull_car_string = [""]

# standard fees / defaults
sales_tax = float(6.75)
daily_fee = float(9.99)
dw_fee = float(18.99)
gas_refill = float(3.913)
ins_fee = float(14.99)
add_milage = float(0.99)
daily_milage = int(100)


while menu_selection <= 6: 
    #print car options
    for i in range(menu_start,menu_stop,menu_myinc):
        print menu_main[i]

    menu_selection = input('Enter your seletion (1,2,3): ')
    print('You\'ve Selected ', menu_selection)

    #Use branches, if, elif, and else
    if (menu_selection == 1 or menu_selection ==2):
        print "1 or 2 selected"
        for i in range(car_start,car_stop,car_myinc):
            print (" ", i, cars[i])
        print "  \n\n"
        car_selection = input('Select your car:')
        print('Selected Car: ', car_selection)
        car_string = cars[i]
        pull_car_string = car_string.split(",")
        pc_start = int(0)
        pc_stop  = len(pull_car_string)
        pc_myinc = int(1)

        #"Nissan LEAF, 5P/1B, REN-4978, 23678, Purple, 50, 55.99"
        car_model = pull_car_string[0]
        car_capacity = pull_car_string[1]
        car_plate = pull_car_string[2]
        car_milage = pull_car_string[3]
        car_color = pull_car_string[4]
        car_fuel_level  = pull_car_string[5]
        daily_fee = pull_car_string[6]
        car_null = ""

    elif (menu_selection == 3):
        print "3rd selection"
        # 1. Collect customer input
        person = input('Enter your name: ')
        print('Hello ', person)
        start_date = input('Enter your start date: ')
        print('Start Date: ', start_date)
        start_time = input('Enter your start time: ')
        print('Start Time: ', start_time )
        return_date = input('Enter your return date: ')
        print('Return Date: ', return_date)
        return_time = input('Enter your return time: ')
        print('Return Time: ', return_time )
        damage_waiver = input('Damage Waiver (Y/N): ')
        print('Damage Waiver: ', damage_waiver)

    elif (menu_selection == 4):
        print "4th selection"
        for x in range(0,receipt_page,1):
            if (x==7):
                print_me = person
            elif (x==8):
                print_me = car_model
            elif (x==9):
                print_me = car_color
            elif (x==10):
                print_me = car_milage
            elif (x==11):
                print_me = car_fuel_level
            elif (x==12):
                print_me = car_plate
            elif (x==13):
                print_me = car_null
            elif (x==16):
                print_me = daily_fee
            elif (x==17):
                print_me = damage_fee, dw_fee
            elif (x==18):
                print_me = ins_fee
            elif (x==19):
                print_me = sales_tax
            elif (x==22):
                print_me = add_milage
            elif (x==23):
                print_me = car_null
            elif (x==24):
                print_me = gas_refill, per_gal
            elif (x==25):
                print_me = daily_milage
            elif (x==28):
                print_me = start_date
            elif (x==29):
                print_me = start_time
            elif (x==30):
                print_me = return_date
            elif (x==31):
                print_me = return_time
            elif (x==34):
                print_me = sub_total
            elif (x==35):
                print_me = sales_tax
            elif (x==36):
                print_me = rental_total           
            else:
                print_me = car_null 

            print ("", receipt_page[x], " ", print_me)
    
    elif (menu_selection == 5): 
        print "5th selection"

    else:
        print "End of program."


