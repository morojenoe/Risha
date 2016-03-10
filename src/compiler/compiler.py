import argparse

from src.grammar import grammar
from src.visitors.pretty_printer import print_visitor


def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file_name', help='a source code file')
    arg_parser.add_argument('-o', nargs='?', default='a.cpp',
                            help='an output file')
    return vars(arg_parser.parse_args())


def read_source_code(file):
    with open(file, 'r') as code:
        return code.read()


def get_input_file_name(settings):
    return settings['file_name']


def get_output_file_name(settings):
    return settings['o']


def generate_cpp(ast, output_file):
    with open(output_file, 'w', encoding='utf-8') as cpp_file:
        visitor = print_visitor.PrintVisitor(cpp_file)
        ast.accept(visitor)


def main():
    settings = parse_args()
    input_file = get_input_file_name(settings)
    output_file = get_output_file_name(settings)
    source_code = read_source_code(input_file)
    lexer = grammar.lexer
    parser = grammar.parser
    ast = parser.parse(input=source_code, lexer=lexer)
    generate_cpp(ast, output_file)


if __name__ == '__main__':
    main()
