from get_morse_code import GetMorseCode

morse_code_generator = GetMorseCode()
print("The symbol/letter which can't be converted will be returned as it is")
to_translate = input("What do you want to translate:  ")
translated_code = morse_code_generator.convert_morse_code(to_translate)
print(f"Your translated code:  {translated_code}")
