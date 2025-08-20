from typing import Optional, Self
from sqlmodel import Field, SQLModel
from pydantic import PositiveInt, model_validator


class ScoreRangeBase(SQLModel):
    range_min: PositiveInt
    range_max: PositiveInt
    label: str = Field(unique=True)

    @model_validator(mode="after")
    def validate_bounds(self) -> Self:
        if self.range_max <= self.range_min:
            raise ValueError("range_max must be greater than range_min")
        return self


class ScoreRange(ScoreRangeBase, table=True):
    __tablename__ = "score_ranges"
    id: Optional[int] = Field(default=None, primary_key=True)


class ScoreRangeCreate(ScoreRangeBase):
    pass


class ScoreRangeRead(ScoreRangeBase):
    id: int
