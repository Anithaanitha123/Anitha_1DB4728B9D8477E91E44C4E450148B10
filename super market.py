from datetime import datetime

name = input("Enter your name: ")
# List of items
lists = '''
KIDS items:
         diaries:
                 silk  Rs 40/each
                 munch Rs 30/each
                kitkat Rs 40/each
           diary milk  Rs 50/each
           icecreams   Rs 60/each
          Toys:
          motor toys   Rs 500/each
          car toys     Rs 1200/each
          baby creams  Rs 400/each
FRUITS items:
             Apple   Rs  220/kg
             banana  Rs  110/kg
        green grapes Rs  60/kg 
        black grapes Rs  70/kg
                goa  Rs  90/kg
              kiwi   Rs  150/kg
              strawberry Rs 60/kg
SNAKES items:
          chips Rs 10/packet
          cookies Rs 30/packet
          lays chips Rs 40/packet
             momos Rs 45/each
             cadberies Rs 60/each
             
 GROCERY items:
             brinjal  Rs 80/kilo
             ladies finger Rs 90/kilo
             coocumber Rs 20/each
             mushroom  Rs 200/packet
             cabbage  Rs 60/each
             califlour Rs 70/each
             tomato   Rs   50/kilo
             onion    Rs   25/kilo
             garlic   Rs   250/kilo
             ginger   Rs   10/each
             curd     Rs    10/each
             butter   Rs    100/each
             butter milk Rs  10/each
             cheese   Rs    40/each
             milk     Rs    41/litre
            dry nuts  Rs    60/packet
            salt      Rs    40/kg
            chilli    Rs    60/kg
            broom     Rs    35/each
        bathing soap Rs  60/each
            brush      Rs     20/each
            washing soap   Rs    40/each
            cooking oil   Rs    200/liter
            hair oil   Rs    60/each
            shampoo     Rs   90/each
            rice      Rs      1200/each
            '''
            
             
         
     


# Declaration
price = 0
pricelist = []
totalprice = 0
finalamount = 0
ilist = []
qlist = []
plist = []

# Rates for items
items = {'silk':40,'munch':30,'kitkat':40,'diary milk':50,'ice creams':60,
         'motor toys':500,'car toys':1200,'baby creams':400,'apple':220,
         'banana':110,'green grapes':60,'black grapes':70,'goa':90,
         'kiwi':150,'strawberry':60,'chips':10,'cookies':30,
         'lays chips':40,'momos':45,'cadberries':60,'brinjal':80,
         'ladies finger':90,'coocumber':20,'mushroom':200,'cabbage':60,
         'califlour':70,'tomato':50,'onion':25,'garlic':250,'ginger':10,
         'curd':10,'butter':100,'butter milk':10,'cheese':40,'milk':41,
         'dry nuts':60,'salt':40,'chilli':40,'broom':35,'bathing soap':60,
         'brush':20,'washing soap':40,'cooking oil':200,'hair oil':60,
         'shampoo':90,'rice':1200}
        
option = int(input("For list of items press 1: "))
if option == 1:
    print(lists)

while True:
    inp1 = int(input("If you want to buy press 1 or 2 for exit: "))
    if inp1 == 2:
        break
    elif inp1 == 1:
        item = input("Enter your item: ").lower()
        quantity = int(input("Enter quantity: "))
        if item in items.keys():
            price = quantity * items[item]
            pricelist.append((item, quantity, price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
        else:
            print("Sorry, the item you entered is not available.")
    else:
        print("You entered the wrong number.")

gst = (totalprice * 5) / 100
finalamount = gst + totalprice

inp = input("Can I bill the items? Yes or No: ").lower()
if inp == 'yes' and finalamount != 0:
    print(25 * "=", "Welcome to Royal Supermarket", 25 * "=")
    print(28 * " ", "Anitha")
    print("Name:", name, "Date:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(75 * "-")
    print("S.No", "Items", "Quantity", "Price")
    for i in range(len(pricelist)):
        print(i + 1, ilist[i], qlist[i], plist[i])
    print(75 * "-")
    print(50 * " ", 'Total Amount:', 'Rs', totalprice)
    print("GST Amount", 'Rs', gst)
    print(75 * "-")
    print(50 * " ", 'Final Amount:', 'Rs', finalamount)
    print(75 * "-")
    print(20 * "-", "Thanks for coming!")
    print(75 * "-")