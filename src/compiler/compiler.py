import argparse

import src.grammar.grammar
import src.ast_visitors.pretty_printer.print_visitor as print_visitor
import src.ast_visitors.class_forward_declaration_printer as cls_forward_decl
import src.ast_visitors.tools.classes as tools_classes


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


def _write_comments(comments, output_file):
    output_file.write('/*\n')
    for comment in comments:
        output_file.write(' * ' + comment + '\n')
    output_file.write(' */\n')


def write_comments(comments, output_file):
    if isinstance(comments, str):
        _write_comments([comments], output_file)
    else:
        _write_comments(comments, output_file)


def write_includes(output_file):
    with open('../../lib/includes.h', 'r') as includes:
        output_file.writelines(includes.readlines())
    output_file.write('\n')


def write_forward_class_declarations(ast, cpp_file):
    write_comments('class declarations', cpp_file)
    visitor = cls_forward_decl.ClassForwardDeclarationVisitor()
    ast.accept_before_after(visitor)
    printer = print_visitor.PrintVisitor(cpp_file)
    class_declarations = tools_classes.make_class_declarations(
        visitor.get_classes())
    class_declarations.accept_print_visitor(printer)


def write_function_declarations(ast, cpp_file):
    pass


def write_class_declaration(ast, cpp_file):
    pass


def write_data(ast, cpp_file):
    pass


def write_function_definitions(ast, cpp_file):
    pass


def write_class_definitions(ast, cpp_file):
    pass


def write_solution(ast, cpp_file):
    visitor = print_visitor.PrintVisitor(cpp_file)
    ast.accept_print_visitor(visitor)


def write_main_function(cpp_file):
    main_function = (
        'int main() {\n',
        '  solution::main();\n',
        '  return 0;\n',
        '}\n',
    )
    cpp_file.writelines(main_function)


def generate_cpp(ast, output_file):
    with open(output_file, 'w', encoding='utf-8') as cpp_file:
        write_includes(cpp_file)
        cpp_file.write('namespace solution {\n\n')
        write_forward_class_declarations(ast, cpp_file)
        write_function_declarations(ast, cpp_file)
        write_class_definitions(ast, cpp_file)
        write_data(ast, cpp_file)
        write_function_definitions(ast, cpp_file)
        write_class_definitions(ast, cpp_file)
        write_solution(ast, cpp_file)
        cpp_file.write('\n}\n\n')
        write_main_function(cpp_file)


def main():
    settings = parse_args()
    input_file = get_input_file_name(settings)
    output_file = get_output_file_name(settings)
    source_code = read_source_code(input_file)
    lexer = src.grammar.grammar.lexer
    parser = src.grammar.grammar.parser
    ast = parser.parse(input=source_code, lexer=lexer)
    generate_cpp(ast, output_file)


if __name__ == '__main__':
    main()
