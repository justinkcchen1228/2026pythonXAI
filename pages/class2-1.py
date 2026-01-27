# 比較運算子，只能同樣類型作比較
print(1 == 1) # True
print(1 != 1) # False
print(1 > 1) # False
print(1 < 1) # False
print(1 >= 1) # True
print(1 <= 1) # True

# 邏輯運算子
# and運算子，只要有一個條件為False，結果就是False
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# or運算子，只要有一個條件為True，結果就是True
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

# not運算子
print(not True) # False
print(not False) # True

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取整數
# 4. + - 加減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or
