import argparse
import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description='Temperature Converter - Convert between Celsius and Fahrenheit',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python converter.py --celsius 25
  python converter.py --fahrenheit 77
  python converter.py -c 0
  python converter.py -f 32
        """
    )

    temp_group = parser.add_mutually_exclusive_group(required=True)

    temp_group.add_argument(
        '-c', '--celsius',
        type=float,
        help='Temperature in Celsius to convert to Fahrenheit'
    )

    temp_group.add_argument(
        '-f', '--fahrenheit',
        type=float,
        help='Temperature in Fahrenheit to convert to Celsius'
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='Temperature Converter v1.0'
    )

    args = parser.parse_args()

    try:
        if args.celsius is not None:
            fahrenheit = celsius_to_fahrenheit(args.celsius)
            print("Temperature Conversion Result:")
            print(f"   {args.celsius}°C = {fahrenheit:.2f}°F")
            if args.celsius <= 0:
                print("   Freezing point of water or below!")
            elif args.celsius >= 100:
                print("   Boiling point of water or above!")
            elif 20 <= args.celsius <= 25:
                print("   Comfortable room temperature!")

        elif args.fahrenheit is not None:
            celsius = fahrenheit_to_celsius(args.fahrenheit)
            print("Temperature Conversion Result:")
            print(f"   {args.fahrenheit}°F = {celsius:.2f}°C")
            if args.fahrenheit <= 32:
                print("   Freezing point of water or below!")
            elif args.fahrenheit >= 212:
                print("   Boiling point of water or above!")
            elif 68 <= args.fahrenheit <= 77:
                print("   Comfortable room temperature!")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
