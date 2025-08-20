import pytest
from pydantic import ValidationError

from app.db.models.score_range import (
    ScoreRange,
    ScoreRangeBase,
)


class TestScoreRangeBase:
    """Test cases for ScoreRangeBase model"""

    def test_instance_creation(self):
        """Test creating a ScoreRangeBase instance"""
        score_range = ScoreRangeBase(range_min=401, range_max=410, label="401-410")

        assert score_range.range_min == 401
        assert score_range.range_max == 410
        assert score_range.label == "401-410"

    def test_invalid_range_bounds(self):
        """Test ValidationError on range_max <= range_min"""
        with pytest.raises(ValidationError):
            ScoreRangeBase(range_min=10, range_max=1, label="10-1")

    def test_equal_range_bounds(self):
        """Test ValidationError on range_max == range_min"""
        with pytest.raises(ValidationError):
            ScoreRangeBase(range_min=400, range_max=400, label="400-400")

    def test_positive_integers_only(self):
        """Test ValidationError on non-positive integers"""
        with pytest.raises(ValidationError):
            ScoreRangeBase(range_min=0, range_max=410, label="Zero Min")

        with pytest.raises(ValidationError):
            ScoreRangeBase(range_min=-1, range_max=410, label="Negative Min")

        with pytest.raises(ValidationError):
            ScoreRangeBase(range_min=401, range_max=0, label="Zero Max")

    def test_label_required(self):
        """Test ValidationError on missing field"""
        with pytest.raises(ValidationError):
            ScoreRangeBase(range_min=401, range_max=410)


class TestScoreRange:
    """Test cases for ScoreRange model"""

    def test_valid_instance_creation(self):
        """Test creating a ScoreRange instance"""
        score_range = ScoreRange(range_min=401, range_max=410, label="401-410")

        assert score_range.range_min == 401
        assert score_range.range_max == 410
        assert score_range.label == "401-410"
        assert score_range.id is None
