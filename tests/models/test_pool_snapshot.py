from datetime import date
import pytest
from app.db.models import PoolSnapshotBase


class TestPoolSnapshotBase:
    """Test cases for PoolSnapshotBase model"""

    def test_instance_creation(self):
        """Test creating a PoolSnapshotBase instance"""
        snapshot = PoolSnapshotBase(date=date(2024, 1, 15), total_candidates=1500)

        assert snapshot.date == date(2024, 1, 15)
        assert snapshot.total_candidates == 1500

    def test_negative_canidates(self):
        """Test ValueError on negative number of candidates"""
        with pytest.raises(ValueError):
            PoolSnapshotBase(date=date(2024, 1, 15), total_candidates=-1)
