"""
Placeholder for document ingestion and indexing.
Future: extract text (e.g. PyMuPDF/PyPDF), chunk, embed, and store in FAISS index.
"""

# TODO: Add document processing (PDF/text). Do not implement embeddings/FAISS here yet.


def ingest_document(file_path, metadata=None):
    """
    Stub: process a document and add to the retrieval index. Not implemented.
    """
    raise NotImplementedError("Document ingestion not implemented yet.")


def list_ingested_documents():
    """Stub: return list of indexed documents for UI. Remove when ingest is implemented."""
    return []
