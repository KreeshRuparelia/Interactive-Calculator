import calculator_operations as c

# ===============================================
# Testing function operationSquared()

# Base Case
assert c.operationSquared("3") == '9'

# Edge Case
assert c.operationSquared("-5.698") == '32.467204'

# ===============================================
# Testing function sortingLists()

# Base Case
assert c.sortingLists("99+43") == ('43', ['null', '+'], ['99', '43'])

# Edge Case
assert c.sortingLists("4000×4÷2+1000–500") == ('500', ['null', '×', '÷', '+', '–'], ['4000', '4', '2', '1000', '500'])

# ===============================================
# Testing function initalOperation()

# Base Case
assert c.initialOperation(0, 1, "", ["56", "2"], ["null", "+"]) == (1, 2, '58.0', ['56', '2'], ['null', '+'])

# Edge Case
assert c.initialOperation(0, 1, "", ["75", "5", "19", "2"], ["null", "÷", "+", "–"]) == (1, 2, '15.0', ['75', '5', '19', '2'], ['null', '÷', '+', '–'])

# ===============================================
# Testing function operationAdd()

# Base Case
assert c.operationAdd("95", 1, ["93", "39", "42", "34"]) == '137.0'

# Edge Case
assert c.operationAdd("-5", 2, ["32", "43", "67", "92.79", "84"]) == '87.79'

# ===============================================
# Testing function operationSubtract()

# Base Case
assert c.operationSubtract("100", 2, ["42", "32", "69", "93", "201"]) == '7.0'

# Edge Case
assert c.operationSubtract("12", 1, ["31", "41", "15.6", "17"]) == '-3.6'

# ===============================================
# Testing function operationMultiply()

# Base Case
assert c.operationMultiply("73", 1, ["13", "26", "70", "99", "181"]) == '5110.0'

# Edge Case
assert c.operationMultiply("-3.1", 1, ["32", "4.7", "3.55", "23.5"]) == '-11.005'

# ===============================================
# Testing function operationDivide()

# Base Case
assert c.operationDivide("65", 2, ["34", "74", "59", "5"]) == '13.0'

# Edge Case
assert c.operationDivide("3.568", 1, ["5.7", "3.09", "5.369"]) == '0.6645557831998511'

# ===============================================
# Testing function operationEquals()

# Base Case
assert c.operationEquals("4000×4÷2+1000–500", 0, 1, "") == '8500' 

# Edge Case
assert c.operationEquals("874.5736×5.34÷4.67+10.093–50.498", 0, 1, "") == '959.64275675'