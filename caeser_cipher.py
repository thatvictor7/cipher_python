cipher = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "10": "j",
    "11": "k",
    "12": "l",
    "13": "m",
    "14": "n",
    "15": "o",
    "16": "p",
    "17": "q",
    "18": "r",
    "19": "s",
    "20": "t",
    "21": "u",
    "22": "v",
    "23": "w",
    "24": "x",
    "25": "y",
    "26": "z"
}

# function to return key for any value
def get_key_by_value(val, obj):
    for key, value in obj.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def string_iterator(string,shift):
    string = string.lower()
    sipher_text = ""
    for i in string:
        if i == ' ':
            sipher_text = sipher_text + ' '
        elif i == ',' or i == '.':
            sipher_text = sipher_text + i
        else:
            sipher_text = sipher_text + char_converter(i,shift)
    print(sipher_text)

def char_converter(string,shift):
    ciphered_key = int(get_key_by_value(string, cipher)) - shift
    ciphered_key = ciphered_key + 26 if ciphered_key <= 0 else ciphered_key
    return cipher.get(str(ciphered_key))

string_iterator("my NAME, is Victor.", 7)