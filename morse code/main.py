from MORSECODE import MorseCode

codes = MorseCode().morse_code

# changing input value to string and everything in upper
print("spaces are converted to '/' for easy readability")
to_convert = str(input("Enter what you want to convert into morse code : ")).upper()

for n in to_convert:
    try:
        if n != " ":
            to_convert = to_convert.replace(n, codes[n])

        elif n == " ":
            to_convert = to_convert.replace(n, "/")
        print(to_convert)
    except KeyError:
        print(f"this({n}) isn't in morse code, \n"
              f"Morse code have limited amount of symbols, cause proper grammar isn't first priority in war")
        break
