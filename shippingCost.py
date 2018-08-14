"""
Zach Miller
9/23/2013
Shipping cost
"""
#asks user for the weight of the package and passes the weight to getCost
def main():
    packageWeight=int(input('Please enter the weight of the package: '))
    getCost(packageWeight)

#determines the cost of the shipping based on the weight of the package
#then passes the cost to displayCost
def getCost(weight):
    cost=0.0
    if(weight>10):
        cost=3.80
    elif(weight>6):
        cost=3.70
    elif(weight>2):
        cost=2.20
    else:
        cost=1.10
    displayCost(cost)

#displays the cost of the package
def displayCost(shippingCost):
    print('Shipping charge: $',format(shippingCost,'.2f'))

#main
main()
