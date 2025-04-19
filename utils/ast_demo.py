# ref: https://docs.python.org/zh-cn/3/library/ast.html#
import ast

def demo():
    node = ast.parse("a = 10")
    print(ast.dump(node))


# Module(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=10))])
if __name__ == "__main__":
    demo()
