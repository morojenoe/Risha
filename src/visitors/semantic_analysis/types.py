class Variable:
    def __init__(self, identifier, variable_type):
        self.identifier = identifier
        self.variable_type = variable_type


class VariableType:
    def __init__(self, cv_qualifier, storage_qualifier, reference_qualifier, var_type):
        self.cv_qualifier = cv_qualifier
        self.storage_qualifier = storage_qualifier
        self.reference_qualifier = reference_qualifier
        self.var_type = var_type


class Function:
    def __init__(self, identifier, return_type, parameters):
        self.identifier = identifier
        self.return_type = return_type
        self.parameters = parameters
