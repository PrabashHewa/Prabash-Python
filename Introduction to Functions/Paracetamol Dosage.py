"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""

def calculate_dose(weight, time, total_dose_24):
    """
    Calculates the appropriate dose of Paracetamol to administer to a patient.

    Parameters:
    weight : The patient's weight in kilograms.
    time : The time in full hours since the last dose was administered.
    total_dose_24 : The total dose of Paracetamol the patient has received in the last 24 hours in milligrams.

    Returns:The dose of Paracetamol to administer, in milligrams.
    Ensures the dose does not exceed the maximum allowed daily dose of 4000 mg.
    """
    if time < 6:
        return 0

    dose_per_kg = 15
    max_dose = weight * dose_per_kg
    remaining_dose = 4000 - total_dose_24

    if remaining_dose <= 0:
        return 0
    dose_to_give = min(max_dose, remaining_dose)
    
    return dose_to_give

def main():
    
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_dose_24 = int(input("The total dose for the last 24 hours (mg): "))
    dose = calculate_dose(weight, time, total_dose_24)
    
    print(f"The amount of Parasetamol to give to the patient: {dose}")

if __name__ == "__main__":
    main()
