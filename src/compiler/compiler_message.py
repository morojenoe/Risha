import enum


class MessageType(enum.Enum):
    ERROR = enum.auto()
    WARNING = enum.auto()


class CompilerMessage:
    def __init__(self, msg_type, row, col, message):
        self.type = msg_type
        self.row = row
        self.col = col
        self.message = message
