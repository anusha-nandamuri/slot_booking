import dataclasses

@dataclasses.dataclass
class UserIdentityDto:
    user_id: int
    is_admin: bool