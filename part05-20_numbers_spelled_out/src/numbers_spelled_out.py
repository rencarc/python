def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    num_to_words = {}
    for i in range(100):
        if i < 10:
            num_to_words[i] = ones[i]
        elif i < 20:
            num_to_words[i] = teens[i - 10]
        else:
            ten_part = tens[i // 10]

            one_part = ones[i % 10] if i % 10 != 0 else ""  
            num_to_words[i] = ten_part + ("-" + one_part if one_part else "")

    return num_to_words


