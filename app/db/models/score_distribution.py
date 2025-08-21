from typing import Optional
from sqlmodel import Field, SQLModel


class ScoreDistributionBase(SQLModel):
    snapshot_id: int = Field(foreign_key="pool_snapshots.id")
    range_id: int = Field(foreign_key="score_ranges.id")
    candidates: int = Field(ge=0)


class ScoreDistribution(ScoreDistributionBase, table=True):
    __tablename__ = "score_distributions"
    id: Optional[int] = Field(default=None, primary_key=True)


class ScoreDistributionCreate(ScoreDistributionBase):
    pass


class ScoreDistributionRead(ScoreDistributionBase):
    id: int
