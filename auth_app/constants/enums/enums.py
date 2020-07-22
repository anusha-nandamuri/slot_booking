import enum
from ib_common.constants import BaseEnumClass


class Gender(BaseEnumClass, enum.Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"
    OTHER = "OTHER"
