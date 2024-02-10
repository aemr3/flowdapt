from uuid import UUID, uuid4
from datetime import datetime

from flowdapt.lib.utils.model import BaseModel, Field as PydanticField


class V1Alpha1ResourceMetadata(BaseModel):
    uid: UUID = PydanticField(default_factory=uuid4)
    name: str
    created_at: datetime = PydanticField(default_factory=datetime.now)
    updated_at: datetime = PydanticField(default_factory=datetime.now)
    annotations: dict[str, str] = {}
