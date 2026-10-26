"""
Program: Temperature Converter
Description: Celsius temperature is converted to Fahrenheit, and it is validated.
Author: Teresa Brown
References: Formula logic sourced from GeeksforGeeks. Code structure optimized 
            with instructional debugging assistance from Gemini AI.
"""

def convert_celsius_to_fahrenheit():
    print("--- Celsius to Fahrenheit Converter ---")
    
    # REQUIREMENT 3 & 5: Continuous loop with try/except validation
    while True:
        user_input = input("Enter temperature in Celsius: ").strip() # Cleans whitespace
        
        try:
            Celsius = float(user_input)
            break # Valid number received, break the loop safely!
        except ValueError:
            # Friendly error message prevents program crashes
            print(f"Error: '{user_input}' is not a valid number. Please try again.\n")

    # The Mathematical Core
    fahrenheit = (Celsius * 9/5) + 32
    
    # REQUIREMENT 4: String Operation 1 (Transformation using float placeholders)
    result_msg = f"{Celsius:.1f}°C is equal to {fahrenheit:.1f}°F."
    print("\n" + result_msg)
    
    # REQUIREMENT 4: String Operation 2 (Analysis counting the tokens in the string)
    words = result_msg.split()
    print(f"(Output Analysis: Message length is {len(words)} tokens.)")

if __name__ == "__main__":
    convert_celsius_to_fahrenheit()
