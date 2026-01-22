from .ingest import ingest_for_user
from .data_version import data_version
from .cache_service import cache_service
import threading


class IngestionService:
    def ingest_async(self, user_id: int):
        def task():
            ingest_for_user(user_id)
            data_version.increment(user_id)
            cache_service.invalidate_user(user_id)

        thread = threading.Thread(target=task, daemon=True)
        thread.start()


ingestion_service = IngestionService()
