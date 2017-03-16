import argparse
import logging
import pathlib

import src.grammar.grammar
import src.ast_visitors
import src.risha_ast
import src.ast_visitors.semantic_analysis
import src.compiler.compiler_message as compiler_message
import src.ast_visitors.semantic_analysis.scope_table as scope_table_env
import src.ast_visitors.semantic_analysis.type_table as type_table_env
import src.ast_visitors.semantic_analysis.tools as semantic_analysis_tools


def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file_name', help='a source code file')
    arg_parser.add_argument('-o', nargs='?', default='a.cpp',
                            help='an output file')
    return vars(arg_parser.parse_args())


def get_filename(path):
    return pathlib.Path(path).name


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
    write_comments('forward class declarations', cpp_file)
    class_visitor = src.ast_visitors.ClassWalker()
    ast.accept_before_after(class_visitor)
    print_visitor = src.ast_visitors.PrintVisitor(cpp_file)
    class_declarations = src.ast_visitors.make_class_forward_declarations(
        class_visitor.get_classes())
    class_declarations.accept_print_visitor(print_visitor)


def write_function_declarations(ast, cpp_file):
    write_comments('function declarations', cpp_file)
    function_visitor = src.ast_visitors.FunctionWalker()
    ast.accept_before_after(function_visitor)
    function_declarations = src.ast_visitors.make_function_declarations(
        function_visitor.get_functions())
    print_visitor = src.ast_visitors.PrintVisitor(cpp_file)
    function_declarations.accept_print_visitor(print_visitor)


def write_alias_declarations(ast, cpp_file):
    write_comments('alias declarations', cpp_file)
    alias_declarations = src.risha_ast.filter_sequence(
        ast, src.risha_ast.AliasDeclaration)
    alias_declarations = src.ast_visitors.make_alias_declarations(
        list(alias_declarations))
    print_visitor = src.ast_visitors.PrintVisitor(cpp_file)
    alias_declarations.accept_print_visitor(print_visitor)


def write_class_declaration(ast, cpp_file):
    write_comments('class declarations', cpp_file)
    class_visitor = src.ast_visitors.ClassWalker()
    ast.accept_before_after(class_visitor)
    class_declarations = src.ast_visitors.make_class_declarations(
        class_visitor.get_classes())
    print_visitor = src.ast_visitors.PrintVisitor(cpp_file)
    class_declarations.accept_print_visitor(print_visitor)


def write_data(ast, cpp_file):
    write_comments('global data', cpp_file)
    data_visitor = src.ast_visitors.DataWalker()
    ast.accept_before_after(data_visitor)
    data = src.ast_visitors.make_data(list(data_visitor.get_data()))
    print_visitor = src.ast_visitors.PrintVisitor(cpp_file)
    data.accept_print_visitor(print_visitor)


def write_function_definitions(ast, cpp_file):
    write_comments('function definitions', cpp_file)
    function_visitor = src.ast_visitors.FunctionWalker()
    ast.accept_before_after(function_visitor)
    function_definitions = src.ast_visitors.make_function_definitions(
        function_visitor.get_functions())
    print_visitor = src.ast_visitors.PrintVisitor(cpp_file)
    function_definitions.accept_print_visitor(print_visitor)


def write_class_definitions(ast, cpp_file):
    write_comments('class definitions', cpp_file)
    class_visitor = src.ast_visitors.ClassWalker()
    ast.accept_before_after(class_visitor)
    class_definitions = src.ast_visitors.make_class_definitions(
        class_visitor.get_classes())
    print_visitor = src.ast_visitors.PrintVisitor(cpp_file)
    class_definitions.accept_print_visitor(print_visitor)


def write_solution(ast, cpp_file):
    write_forward_class_declarations(ast, cpp_file)
    write_function_declarations(ast, cpp_file)
    write_alias_declarations(ast, cpp_file)
    write_class_declaration(ast, cpp_file)
    write_data(ast, cpp_file)
    write_function_definitions(ast, cpp_file)
    write_class_definitions(ast, cpp_file)


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
        write_solution(ast, cpp_file)
        cpp_file.write('\n} // namespace solution\n\n')
        write_main_function(cpp_file)


def extract_functions_from_ast(ast):
    functions = []
    function_definitions = src.risha_ast.filter_sequence(
        ast, src.risha_ast.FunctionDefinition)
    for function_def in function_definitions:
        functions.append(semantic_analysis_tools.make_function(function_def))
    return functions


def extract_type_from_simple_declaration(simple_declaration, ast_node):
    if not isinstance(simple_declaration, src.risha_ast.SimpleDeclaration):
        logging.getLogger('risha').exception('Parameter must be an instance '
                                             'of risha_ast.SimpleDeclaration ')
        return None
    if simple_declaration.specifiers is None:
        return None
    for specifier in simple_declaration.specifiers:
        if isinstance(specifier, ast_node):
            return specifier
    return None


def extract_types_from_ast(ast, ast_node):
    new_types = []
    simple_declarations = src.risha_ast.filter_sequence(
        ast, src.risha_ast.SimpleDeclaration)
    for simple_decl in simple_declarations:
        some_type = extract_type_from_simple_declaration(simple_decl, ast_node)
        if some_type is not None:
            new_types.append(some_type)
    return new_types


def extract_alias_declarations_from_ast(ast):
    alias_declarations = src.risha_ast.filter_sequence(
        ast, src.risha_ast.AliasDeclaration)
    return list(alias_declarations)


def extract_data_from_ast(ast):
    data = []
    simple_declarations = src.risha_ast.filter_sequence(
        ast, src.risha_ast.SimpleDeclaration)
    for simple_decl in simple_declarations:
        variables = semantic_analysis_tools.make_variables(simple_decl)
        data.extend(variables)
    return data


def check_errors(ast):
    scope_table = scope_table_env.ScopeTable().enter_scope()
    type_table = type_table_env.TypeTable()
    functions = extract_functions_from_ast(ast)
    classes = extract_types_from_ast(ast, src.risha_ast.ClassDefinition)
    enums = extract_types_from_ast(ast, src.risha_ast.EnumDefinition)
    alias_declarations = extract_alias_declarations_from_ast(ast)
    data = extract_data_from_ast(ast)
    semantic_analysis_visitor = \
        src.ast_visitors.semantic_analysis.SemanticAnalysisVisitor(
            scope_table, type_table)
    ast.accept_before_after(semantic_analysis_visitor)
    return semantic_analysis_visitor.get_errors()


def print_errors(messages, filename, source_code):
    def find_column(source, col):
        last_cr = source.rfind('\n', 0, col)
        if last_cr < 0:
            last_cr = 0
        column = col - last_cr
        return column

    source_code_by_lines = source_code.splitlines()

    compiler_messages = {}
    for msg_type in compiler_message.MessageType:
        compiler_messages[msg_type] = []

    for message in messages:
        message.col = find_column(source_code, message.col)
        compiler_messages[message.type].append(message)

    count_errors = len(compiler_messages[compiler_message.MessageType.ERROR])
    count_warnings = len(compiler_messages[
                             compiler_message.MessageType.WARNING])
    logging.getLogger('risha').error('Found {errors} errors, {warns} '
                                     'warnings.'.format(errors=count_errors,
                                                        warns=count_warnings))

    for msg_type in compiler_message.MessageType:
        for message in compiler_messages[msg_type]:
            if message.type == compiler_message.MessageType.ERROR:
                logging.getLogger('risha').error(
                    '{filename}:{row}:{col}: error: {msg}'.format(
                        filename=filename,
                        row=message.row,
                        col=message.col,
                        msg=message.message))
                logging.getLogger('risha').error(
                    source_code_by_lines[message.row - 1])
                logging.getLogger('risha').error(' ' * (message.col - 1) + '^')
            elif message.type == compiler_message.MessageType.WARNING:
                logging.getLogger('risha').warning(
                    '{filename}:{row}:{col}: error: {msg}'.format(
                        filename=filename,
                        row=message.row,
                        col=message.col,
                        msg=message.message))
                logging.getLogger('risha').warning(
                    source_code_by_lines[message.row - 1])
                logging.getLogger('risha').warning(
                    ' ' * (message.col - 1) + '^')


def main():
    settings = parse_args()
    input_file = get_input_file_name(settings)
    output_file = get_output_file_name(settings)
    source_code = read_source_code(input_file)
    lexer = src.grammar.grammar.lexer
    parser = src.grammar.grammar.parser
    ast = parser.parse(input=source_code, lexer=lexer)
    errors = check_errors(ast)
    if len(errors) == 0:
        generate_cpp(ast, output_file)
    else:
        print_errors(errors, get_filename(input_file), source_code)


if __name__ == '__main__':
    main()
