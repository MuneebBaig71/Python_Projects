Amount = int(input("Enter Rent: "))
print("Rent is", Amount)
Days = int(input("Enter Days: "))

# Initialize Rent_in_Advance for days below 30
Rent_in_Advance = round((Amount * 12 / 365) * Days, 2)
print("Rent in Advance is", Rent_in_Advance)

if Days > 31:
    print("Days are more than 31")
    extra_days = Days - 30  # Calculate extra days
    extra_rent = round((Amount * 12 / 365) * extra_days, 2)
    print(f"Rent for extra {extra_days} days is", extra_rent)
else:
    extra_days = 0  # No extra days
    extra_rent = 0.0

Holding_Deposit = round((Amount * 12 / 52), 2)
print("Holding Deposit is", Holding_Deposit)

security_deposit = round((Amount * 12 / 52) * 5, 2)
print("Security Deposit is", security_deposit)

if Days > 31:
    totalrent_inadvance = round(Amount + extra_rent, 2)
    print("Total Rent in Advance is", totalrent_inadvance)
    Total = round(totalrent_inadvance + security_deposit, 2)
    print("Total Rent is", Total)
else:
    Total = round(Rent_in_Advance + security_deposit, 2)
    print("Total Rent is", Total)
print("finished")