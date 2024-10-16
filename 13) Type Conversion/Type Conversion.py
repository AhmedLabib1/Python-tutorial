# Implicit conversion: also known as coercion, is the automatic conversion of a data type into another data type by the interpreter (in interpreted languages)
# or the compiler (in compiled languages) without any explicit instruction from the programmer. This usually happens when mixing different types in expressions.

# Implicit conversion from integer to float
int_var_1 = 5
float_var_1 = 3.14

result1 = int_var_1 + float_var_1 # int_var_1 is implicitly converted to float
print(result1)

# Implicit conversion from integer to complex
int_var_2 = 5
complex_var_1 = 5+3j

result2 = int_var_2 + complex_var_1 # int_var is implicitly converted to complex 
print(result2)

# Mixed Numeric Types: When performing operations involving integers, floats, and complex numbers, Python follows a hierarchy: integer -> float -> complex.
int_var_3 = 5
float_var_2 = 3.14
complex_var_2 = 5+3j

result3 = int_var_3 + float_var_2 + complex_var_2 # int_var is implicitly converted to complex and float_var_2 converted to complex.
print(result3)

# Implicit conversion from boolean to Numeric (int - float - complex)
bool_var_1 = True
int_var_4 = 5

result4 = bool_var_1 + int_var_4 # bool_var_1 is implicitly converted to integer.
print(result4)

# Explicit conversion: also known as type casting, is the manual conversion of one data type to another data type using built-in functions
# or methods provided by the programming language. This is done explicitly by the programmer when they need to ensure the correct type conversion.

# Numeric Type Conversion
x = "10"
y = "20.5"

int_x = int(x)
float_y = float(y)

print(int(x)) # 10
print(float(y)) # 20.5
print(complex(x)) # 10+0j
print(complex(int_x, float_y)) # 10+20.5j

# Sequence Type Conversion
s = "Hello"

print(list(s))
print(tuple(s))
print(set(s)) # Note: set is unordered
print(str(123))

# Mappings
t = [('one', 1), ('two', 2)]
print(dict(t))

# Boolean Type Conversion
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("non-empty string"))  # True

# Other Types
print(chr(97))  # 'a'
print(ord('a'))  # 97
print(hex(255))  # '0xff'
print(oct(8))  # '0o10'
print(bin(3))  # '0b11'