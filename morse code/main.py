from MORSECODE import MorseCode

morse_codes = MorseCode().morse_code


class GetMorseCode():
    def __init__(self):
        pass

    def convert_morse_code(self, string: str):
        string = string.upper()
        for n in string:
            try:
                if n != " ":
                    string = string.replace(n, morse_codes[n])

                elif n == " ":
                    string = string.replace(n, "space")

            except KeyError:
                print(f"this({n}) isn't in morse code, \n"
                      f"Morse code have limited amount of symbols, cause proper grammar isn't first priority in war")

        return string
