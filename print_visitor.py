class PrintVisitor:
    def __init__(self, output):
        self.output = output

    def visit(self, elem):
        print(elem, file=self.output)
