def convert(raw_val):
    value = str(raw_val)

    if value.isdecimal():
        val = int(value)
        binary = ''
        while val != 0:
            binary += str(val%2)
            val //= 2
        
        return binary[::-1]
