import pytest
from app.db.models import ScoreDistributionBase


class TestScoreDistributionBase:
    """Test cases for ScoreDistributionBase model"""

    def test_instance_creation(self):
        """Test creating a ScoreDistributionBase instance"""
        distribution = ScoreDistributionBase(snapshot_id=1, range_id=5, candidates=150)

        assert distribution.snapshot_id == 1
        assert distribution.range_id == 5
        assert distribution.candidates == 150

    def test_negative_canidates(self):
        """Test ValueError on negative number of candidates"""
        with pytest.raises(ValueError):
            ScoreDistributionBase(snapshot_id=1, range_id=5, candidates=-1)
