import enum


class MessageType(enum.Enum):
    WARNING = 1
    ERROR = 2


class CompilerMessage:
    def __init__(self, msg_type, row, col, message):
        self.type = msg_type
        self.row = row
        self.col = col
        self.message = message
