class InvalidPostId(Exception):
    pass


class InvalidLimitValue(Exception):
    def __init__(self, invalid_limit_value: int):
        self.invalid_limit_value = invalid_limit_value


class InvalidOffsetValue(Exception):
    def __init__(self, invalid_offset_value: int):
        self.invalid_offset_value = invalid_offset_value
