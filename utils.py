def testfun(x: int, y: int) -> int:
    return x + y


# 讓人import 客製化程式 讓下方程式不會被執行
if __name__ == "__main__":
    x = 1
    y = 2
    result = testfun(x, y)
    print(result)