import sys
import pint

ur = pint.UnitRegistry()
q = ur.Quantity

lunits = ['kilometer', 'hectometer', 'decameter', 'meter', 'decimeter', 'centimeter', 'millimeter']
tunits= ['celsius', 'fahrenheit', 'kelvin' ,  'rankine']
wunits = ['kilogram', 'hectogram', 'decagram' ,'gram' ,'decigram' ,'centigram' ,'milligram']
vunits = ['milliliter', 'centiliter', 'deciliter', 'liter', 'dekaliter', 'hectoliter', 'kiloliter']

def main():

    #Specific number for specific type of units
    print("Unit Conversion Program:\n1. for Length\n2. for Temperature\n3. for Weight\n4. for Volume\n5. for EXIT")

    #setting the type of units for conversion
    mode = take_input()

    match mode:
        
        case 1:
            print("Length conversion selected")
            from_unit = input("Enter the unit to convert from (e.g., meter): ").strip().lower()
            to_unit = input("Enter the unit to convert from (e.g., kilometer): ").strip().lower()

            if from_unit not in lunits or to_unit not in lunits:
                raise ValueError(sys.exit("Wrong units!"))

            while True:
                try:
                    value = float(input(f"Enter the value in {from_unit}: "))
                    break
                except ValueError:
                    pass

            r = convert_length(from_unit, to_unit,value)

        case 2:
            print("Temperature conversion selected")
            from_unit = input("Enter the unit to convert from (e.g., celsius): ").strip().lower()
            to_unit = input("Enter the unit to convert from (e.g., fahrenheit): ").strip().lower()

            if from_unit not in tunits or to_unit not in tunits:
                raise ValueError(sys.exit("Wrong units!"))
            
            while True:
                try:
                    value = float(input(f"Enter the value in {from_unit}: "))
                    break
                except ValueError:
                    pass

            r = convert_temp(from_unit, to_unit,value)

        case 3:
            print("Weight conversion selected")
            from_unit = input("Enter the unit to convert from (e.g., gram): ").strip().lower()
            to_unit = input("Enter the unit to convert from (e.g., kilogram): ").strip().lower()
            
            if from_unit not in wunits or to_unit not in wunits:
                raise ValueError(sys.exit("Wrong units!"))

            while True:
                try:
                    value = float(input(f"Enter the value in {from_unit}: "))
                    break
                except ValueError:
                    pass

            r = convert_weight(from_unit, to_unit,value)

        case 4:
            print("Volume conversion selected")
            from_unit = input("Enter the unit to convert from (e.g., liter): ").strip().lower()
            to_unit = input("Enter the unit to convert from (e.g., kiloliter): ").strip().lower()

            if from_unit not in vunits or to_unit not in vunits:
                raise ValueError(sys.exit("Wrong units!"))
            
            while True:
                try:
                    value = float(input(f"Enter the value in {from_unit}: "))
                    break
                except ValueError:
                    pass

            r = convert_volume(from_unit, to_unit,value)

        case 5:
            sys.exit("Thank you for using!")
        case _:
            sys.exit("Invalid Input!")

    #output
    print(f"{value} {from_unit} = {r}")


#Taking input
def take_input():

    try:

        inpt = int(input("Select the type of units "))

    except ValueError:
        sys.exit("Invalid Input!")

    else:
        return inpt
    
#Conversion of Length
def convert_length(f, t, value):
    
    r = value * ur(f).to(t)
    return r.magnitude


#Conversion of Temperature
def convert_temp(f, t, value):
     
    match f:
        case "celsius":
            fr = ur.degC
        case "kelvin":
            fr = ur.degK
        case "fahrenheit":
            fr = ur.degF
        case "rankine":
            fr = ur.degR
        case _:
            sys.exit("Invalid input!")

        
    match t:
        case "celsius":
            to = ur.degC
        case "kelvin":
            to = ur.degK
        case "fahrenheit":
            to = ur.degF
        case "rankine":
            to = ur.degR
        case _:
            sys.exit("Invalid input!")


   
    inter = q(value, fr)
    r = inter.to(to)
    return r.magnitude


#Conversion of Weight
def convert_weight(f, t, value):
    
        r = value * ur(f).to(t)
        return r.magnitude


#Conversion of Volume
def convert_volume(f, t, value):
    
        r = value * ur(f).to(t)
        return r.magnitude



    
if __name__ == "__main__":
    main()