import pytest
from pydantic import ValidationError
from app.db.models import ScoreRangeBase


class TestScoreRangeBase:
    """Test cases for ScoreRangeBase model"""

    def test_valid_range_creation(self):
        """Test creating valid score range"""
        score_range = ScoreRangeBase(range_min=401, range_max=410, label="401-410")
        assert score_range.range_min == 401
        assert score_range.range_max == 410

    def test_invalid_range_bounds(self):
        """Test custom validation: range_max must be greater than range_min"""
        with pytest.raises(ValidationError):
            ScoreRangeBase(range_min=410, range_max=401, label="Invalid")

        with pytest.raises(ValidationError):
            ScoreRangeBase(range_min=400, range_max=400, label="Equal")

    def test_equal_range_bounds(self):
        """Custom validation: range_min cannot equal range_max"""
        with pytest.raises(ValidationError):
            ScoreRangeBase(range_min=400, range_max=400, label="Equal")
