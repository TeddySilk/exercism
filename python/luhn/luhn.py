class Luhn:
    def __init__(self, card_num):      
        self.core_num = card_num

        self.luhn_num = [char for char in self.core_num if not char.isspace()]
        self.luhn_num.reverse()

    def valid(self):
        luhn_sum = 0

        if len(self.luhn_num) < 2:
            print(f"Number is too short (less than 2 digits).")
            return False

        check = 0
        for char in self.luhn_num:
            if not char.isnumeric():
                print(f"{char} is not numeric.")
                return False
            if check == 1:
                v = int(char) * 2
                check = 0
            else:
                v = int(char)
                check = 1

            print(v)
            if v > 9:
                v = v - 9    

            luhn_sum += v

        print(f"Luhn Sum: {luhn_sum}")

        if luhn_sum % 10 == 0:
            return True
            
        return False