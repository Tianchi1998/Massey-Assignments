#First,we create the head of this table.
print("                **Sale prices**")
print("Normal price:\t$9.95\t$14.95\t$19.95\t$24.95\t$29.95\t$34.95\t$39.95\t$44.95\t$49.95")
print("---------------------------------------------------------------------------------------")
#Create the lists we need.
normal_price=[9.95,14.95,19.95,24.95,29.95,34.95,39.95,44.95,49.95]
rate=[0.9,0.85,0.8,0.75,0.7,0.65,0.6,0.55,0.5]
#Then we create the first line of this table.
print("\t%%off: 5%%\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t%0.2f"%(9.95*0.95,14.95*0.95,19.95*0.95,24.95*0.95,29.95*0.95,34.95*0.95,39.95*0.95,44.95*0.95,49.95*0.95))
#Use the nested for loop to create other lines.
for percent in rate:
    n=0      #To count times.
    print("         %0.0f%%"%((1-percent)*100),end="")
    for price in normal_price:
        n=n+1
        print("\t%0.2f"%(price*percent),end="")
        if n==9:    #When we come to the last number of a line,create a new line.
            print()
