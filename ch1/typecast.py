"""Type casting demonstration."""

num1 = int("32")      # string to int
num2 = float("3.14")  # string to float
str_num = str(100)    # int to string
truncated_num = int(3.99)   # float to int (truncates decimal part)!!! data loss

# result1 = "Coding" + 7           # TypeError: can only concatenate str (not "int") to str
result2 = "Coding" + str(7)        # Correct way to concatenate string and int
result3 = 5 +3.2                   # int + float results in float