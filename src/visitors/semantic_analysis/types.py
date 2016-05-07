class Variable:
    def __init__(self, identifier, variable_type):
        self.identifier = identifier
        self.variable_type = variable_type

    def __str__(self):
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

    def __str__(self):
        result = '{return_type} {identifier}('.format(
            return_type=self.return_type, identifier=self.identifier)
        for parameter in self.parameters:
            result += '{parameter}, '.format(parameter=parameter)
        if len(self.parameters) > 0:
            result = result[0: len(result) - 2]
        result += ')'
        return result
