from dataclasses import dataclass

@dataclass
class Credentials:
    access_token: str
    expires_in: int
    token_type: str
    scope: str


