from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class AuthRequest:
  """
  Authentication reqeust model
  """
  username: str
  password: str