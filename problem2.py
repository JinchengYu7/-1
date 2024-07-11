def check_parentheses(lines):
    results = []
    for line in lines:
        stack = []
        result_line = [' '] * len(line)
        for i, char in enumerate(line):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    result_line[i] = '?'
        
        while stack:
            result_line[stack.pop()] = 'x'
        
        results.append(''.join(result_line))
    
    return results

# 例子
input_lines = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]
#输出结果
results = check_parentheses(input_lines)
for line, result in zip(input_lines, results):
    print(line)
    print(result)
