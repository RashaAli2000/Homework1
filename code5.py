def is_valid_binary(binary_str):
   
    for char in binary_str:
        if char not in ('0', '1'):
            return False
    return True

def binary_to_decimal(binary_str):
    # تحقق من أن الإدخال يتكون فقط من 0 و 1
    if not all(char in '01' for char in binary_str):
        return "خطأ: أدخل رقماً ثنائياً صالحاً يتكون فقط من 0 و 1."

    # تحويل السلسلة الثنائية إلى عدد عشري
    decimal_number = int(binary_str, 2)
    return decimal_number

def main():
    while True:
        binary_str = input("أدخل رقماً ثنائياً: ").strip()
        
        result = binary_to_decimal(binary_str)
        
        if isinstance(result, int):
            print(f"العدد العشري المكافئ للعدد الثنائي {binary_str} هو {result}.")
            break
        else:
            print(result)
            print("يرجى المحاولة مرة أخرى.")

if __name__ == "__main__":
    main()
