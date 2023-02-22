"""Converts temperatures from F, K, C to K, F, C

Returns:
    int: returns the converted temperature
"""
import functions
from functions import t12; from functions import get_key_press

def temp_convert(input_temp, i_u, o_u):
    input_unit = i_u.upper()
    output_unit = o_u.upper()
    print(input_unit); print(output_unit)
    if input_unit == 'C':
        if output_unit == 'F':
            return (input_temp * 9/5) + 32
        elif output_unit == 'K':
            return input_temp + 273.15
        else:
            return input_temp
    elif input_unit == 'F':
        if output_unit == 'C':
            return (input_temp - 32) / 1.8
        elif output_unit == 'K':
            return (input_temp + 459.67) * 5 / 9
        else:
            return input_temp
    elif input_unit == 'K':
        if output_unit == 'C':
            return input_temp - 273.15
        elif output_unit == 'F':
            return input_temp * 9 / 5 - 459.67
        else:
            return input_temp
    else:
        return input_temp



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Convert temperature between Celsius, Fahrenheit, and Kelvin')

    parser.add_argument('temp', type=float, help='Temperature to be converted')
    parser.add_argument('input_unit', type=str, help='Input unit (C, F, or K)')
    parser.add_argument('output_unit', type=str, help='Output unit (C, F, or K)')

    args = parser.parse_args()
    print(args.temp)
    

    
    
    op_temp = temp_convert(args.temp, args.input_unit, args.output_unit)
    t12(str(op_temp) + "°" + args.output_unit.upper())
