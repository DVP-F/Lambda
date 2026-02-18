from funcs import * # go grab the lambda functions

print(IF(TRUE)("yes")("no"))   # "yes"
print(IF(FALSE)("yes")("no"))  # "no"

ONE  = SUCC(ZERO)
TWO  = SUCC(ONE)
THREE = SUCC(TWO)

print(to_int(ZERO))         # 0
print(to_int(THREE))        # 3
print(to_int(ADD(TWO)(THREE)))   # 5
print(to_int(MULT(TWO)(THREE)))  # 6
