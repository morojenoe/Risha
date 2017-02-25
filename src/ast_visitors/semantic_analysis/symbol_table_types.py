class Variable:
    def __init__(self, identifier, variable_type, default_value):
        assert isinstance(identifier, str)
        self.identifier = identifier
        self.variable_type = variable_type
        self.has_default_value = default_value

    def __str__(self):
        if self.has_default_value:
            return '{type} {name} = default'.format(type=self.variable_type,
                                                    name=self.identifier)
        return '{type} {name}'.format(type=self.variable_type,
                                      name=self.identifier)


class VariableType:
    def __init__(self, cv_qualifier, storage_qualifier,
                 reference_qualifier, var_type):
        self.cv_qualifier = cv_qualifier
        self.storage_qualifier = storage_qualifier
        self.reference_qualifier = reference_qualifier
        self.var_type = var_type

    def __str__(self):
        result = ''
        if self.storage_qualifier is not None:
            result += '{storage_qualifier} '.format(
                storage_qualifier=self.storage_qualifier)
        if self.cv_qualifier is not None:
            result += '{cv_qualifier} '.format(
                cv_qualifier=self.cv_qualifier)
        if self.reference_qualifier is not None:
            result += '{ref_qualifier} '.format(
                ref_qualifier=self.reference_qualifier)
        if self.var_type is not None:
            result += '{type} '.format(type=self.var_type)
        return result.strip()


class Function:
    def __init__(self, identifier, return_type, parameters):
        self.identifier = identifier
        self.return_type = return_type
        self.parameters = parameters

    def parameters_range(self):
        default_params = list(filter(lambda param: param[1].has_default_value,
                                     enumerate(self.parameters)))
        if len(default_params) == 0:
            return len(self.parameters), len(self.parameters)
        return default_params[0][0], len(self.parameters)

    def __str__(self):
        result = '{return_type} {identifier}('.format(
            return_type=self.return_type, identifier=self.identifier)
        for parameter in self.parameters:
            result += '{parameter}, '.format(parameter=parameter)
        if len(self.parameters) > 0:
            result = result[0: len(result) - 2]
        result += ')'
        return result


class VariableTypeSpecifier:
    def __init__(self, identifier, *template_args):
        self.identifier = identifier
        self.template_args = tuple(template_args)

    def __eq__(self, other):
        return (self.identifier == other.identifier and
                self.template_args == other.template_args)

    def __ne__(self, other):
        return (self.identifier != other.identifier or
                self.template_args != other.template_args)

    def __hash__(self):
        return hash((self.identifier, self.template_args))
