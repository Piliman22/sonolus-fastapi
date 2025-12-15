from pydantic import BaseModel
from typing import Optional

class SonolusContext(BaseModel):
    user_session: Optional[str] = None
    is_dev: bool = False