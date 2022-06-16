import json

if __name__ == "__main__":

    with open("international_morse_code.json", "r") as f:
        mapping_rules = json.load(f)

    input_string = input("Enter text(alphanumeric characters) to translate: ")
    output_list = [mapping_rules.get(c.upper()) for c in input_string]
    output_string = " ".join(output_list)
    print(f"Morse code is {output_string}")
