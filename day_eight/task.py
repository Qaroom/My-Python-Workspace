letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def get_parametres():
    direction = input("Write what operation you need (encode or decode)\n").lower()
    text = list(input(f"type your message which you need to {direction}\n"))
    pass_step = int(input("enter your code step\n"))
    print(text)
    return direction, text, pass_step

def decode_or_incode_text(direction, text, pass_step):
    encode_name = [] 
    decode_name = []  

    if direction == "encode":
        for alphabet in text:
            index = (letter.index(alphabet) + pass_step) % len(letter)  
            encode_name.append(letter[index])
        print(f"your encoded text is {''.join(encode_name)}")

    elif direction == "decode":
        for alphabet in text:
            index = (letter.index(alphabet) - pass_step) % len(letter) 
            decode_name.append(letter[index])
        print(f"your decoded text is {''.join(decode_name)}")

    else:
        print("wrong operation name")

def main():
    while True:
        direction, text, pass_step = get_parametres()
        decode_or_incode_text(direction, text, pass_step)

        operation_control = input("Do you want another operation? (yes or no)\n").lower()  # ✅ added ()

        if operation_control == "no":
            print(f"{direction} operation has been completed, thank you")
            break

if __name__ == "__main__":
    main()