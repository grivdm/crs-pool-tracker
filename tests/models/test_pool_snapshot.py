from datetime import date
from app.db.models.pool_snapshot import PoolSnapshotBase


class TestPoolSnapshotBase:
    """Test cases for PoolSnapshotBase model"""

    def test_instance_creation(self):
        """Test creating a PoolSnapshotBase instance"""
        snapshot = PoolSnapshotBase(date=date(2024, 1, 15), total_candidates=1500)

        assert snapshot.date == date(2024, 1, 15)
        assert snapshot.total_candidates == 1500
