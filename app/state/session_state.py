from dataclasses import dataclass
from typing import Optional


@dataclass
class SessionState:

    workflow: Optional[str] = None

    run_id: Optional[int] = None

    branch: Optional[str] = None

    status: Optional[str] = None

    platform: Optional[str] = None