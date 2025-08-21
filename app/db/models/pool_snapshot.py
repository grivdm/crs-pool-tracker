from datetime import date
from typing import Optional
from sqlmodel import Field, SQLModel


class PoolSnapshotBase(SQLModel):
    date: date
    total_candidates: int = Field(ge=0)


class PoolSnapshot(PoolSnapshotBase, table=True):
    __tablename__ = "pool_snapshots"
    id: Optional[int] = Field(default=None, primary_key=True)


class PoolSnapshotCreate(PoolSnapshotBase):
    pass


class PoolSnapshotRead(PoolSnapshotBase):
    id: int
