import argparse
import grammar
import cpl_ast_traverse


def get_file_name():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file_name', help='a source code file')
    args = vars(arg_parser.parse_args())
    return args['file_name']


def read_source_code(file):
    with open(file, 'r') as code:
        return code.read()


if __name__ == '__main__':
    file_name = get_file_name()
    source_code = read_source_code(file_name)
    lexer = grammar.lexer
    parser = grammar.parser
    ast = parser.parse(input=source_code, lexer=lexer)
    assert isinstance(file_name, str)
    cpl_ast_traverse.generate_cpp(ast, 'test.cpp')
