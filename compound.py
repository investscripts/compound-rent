#!/usr/bin/python

IA = int(input("Initial Amount "))
print("Starting With $", IA,"USD")

Num_Months = int(input("Number Of Months To Calculate "))
print("Calculating", Num_Months, "Months")

contributions = int(input("Expected Monthly Personal Contributions "))

print("You're contributing $",contributions,"USD Monthly")

external_contribution = int(input("Monthly Rental Cashflow "))

total = previous_50k = IA
for i in range(1,Num_Months):
    print("Month",i, "$"+ str(total))
    total += contributions + external_contribution
    if total - previous_50k >= 50000 :
        external_contribution += 1000
        print(
            "Rental Cashflow Increased by 1000 USD! Cashflow contributions are now $",
            external_contribution,
            "/ month!",
        )
        previous_50k = total
