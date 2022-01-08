# Checking if the value is binary
def is_binary(val):
    for character in val:
        if character not in ('1', '0'):
            return False
    return True

def convert(binary):
    bin = str(binary)
    if is_binary(bin):
        decimal = 0
        power = 0
        # Start from the last bit
        for character in bin[::-1]:
            # The method everyone learns at school.
            # 101 = 1*2^2 + 0*2^1 + 1*2^0 ==> 5
            decimal += int(character) * (2**power)
            power+=1
        return decimal
    else:
        # If the given value is not binary, return NoneType
        return 
    
    