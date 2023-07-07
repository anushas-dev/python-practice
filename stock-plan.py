days = int(input())
stock_prices = list(map(int, input().split()))
n = len(stock_prices)
stack = []
stock_span = [0] * n
stack.append(0)
stock_span[0] = 1
for i in range(1, n):
    while len(stack) > 0 and stock_prices[i] >= stock_prices[stack[-1]]:
        stack.pop()
    stock_span[i] = i + 1 if len(stack) == 0 else i - stack[-1]
    stack.append(i)

print(stock_span)