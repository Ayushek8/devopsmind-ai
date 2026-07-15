from enum import Enum


class ActionType(str, Enum):

    READ = "read"

    WRITE = "write"
