import dataclasses

@dataclasses.dataclass
class AuthenticationDto:
    access_token: str
    is_admin: bool