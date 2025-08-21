from typing import Optional
from sqlmodel import Field, SQLModel, Relationship

from app.db.models import ScoreRange, PoolSnapshot


class ScoreDistributionBase(SQLModel):
    snapshot_id: int = Field(foreign_key="pool_snapshots.id")
    range_id: int = Field(foreign_key="score_ranges.id")
    candidates: int = Field(ge=0)


class ScoreDistribution(ScoreDistributionBase, table=True):
    __tablename__ = "score_distributions"
    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    snapshot: "PoolSnapshot" = Relationship(back_populates="score_distributions")
    score_range: "ScoreRange" = Relationship(back_populates="score_distributions")


class ScoreDistributionCreate(ScoreDistributionBase):
    pass


class ScoreDistributionRead(ScoreDistributionBase):
    id: int
