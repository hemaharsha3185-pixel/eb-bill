# Full EB Bill Calculation (TNEB Domestic Tariff)

def calculate_eb_bill(units):
    fixed_charge = 0
    energy_charge = 0

    # Fixed charges based on consumption slabs
    if units <= 100:
        fixed_charge = 0
    elif units <= 200:
        fixed_charge = 20
    elif units <= 500:
        fixed_charge = 30
    else:
        fixed_charge = 50

    # Energy charges (slab-wise)
    if units <= 100:
        energy_charge = 0  # Fully subsidized
    elif units <= 200:
        energy_charge = (units - 100) * 2.25
    elif units <= 500:
        energy_charge = (100 * 2.25) + (units - 200) * 4.50
    else:
        energy_charge = (100 * 2.25) + (300 * 4.50) + (units - 500) * 6.00

    total_bill = fixed_charge + energy_charge
    return fixed_charge, energy_charge, total_bill


# Main Program
units = float(input("Enter units consumed: "))

fixed, energy, total = calculate_eb_bill(units)

print("\n----- EB BILL DETAILS -----")
print("Units Consumed:", units)
print("Fixed Charges: ₹", fixed)
print("Energy Charges: ₹", energy)
print("Total EB Bill: ₹", total)
