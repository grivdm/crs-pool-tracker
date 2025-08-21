from datetime import date
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

from app.db.models import ScoreDistribution


class PoolSnapshotBase(SQLModel):
    date: date
    total_candidates: int = Field(ge=0)


class PoolSnapshot(PoolSnapshotBase, table=True):
    __tablename__ = "pool_snapshots"
    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    score_distributions: List["ScoreDistribution"] = Relationship(
        back_populates="snapshot"
    )


class PoolSnapshotCreate(PoolSnapshotBase):
    pass


class PoolSnapshotRead(PoolSnapshotBase):
    id: int
