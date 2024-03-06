def check_parentheses(input_str):
    stack = []
    result = ""

    for i, char in enumerate(input_str):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result += '?' * i + 'x'

    for index in stack:
        result += 'x' * index

    return result + input_str

# 示例调用
input_strings = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

for string in input_strings:
    print(check_parentheses(string))
