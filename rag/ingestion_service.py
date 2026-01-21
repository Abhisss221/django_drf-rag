import threading
from .ingest import ingest_for_user


class IngestionService:
    def ingest_async(self, user_id: int):
        """
        Runs ingestion in a background thread.
        """
        thread = threading.Thread(
            target=ingest_for_user,
            args=(user_id,),
            daemon=True
        )
        thread.start()


ingestion_service = IngestionService()
