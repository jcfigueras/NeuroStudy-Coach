"""
Minimal SQLite connection helper for NeuroStudy Coach.
Extend with connection pooling, context managers, and schema initialization as needed.
"""

import sqlite3
from pathlib import Path

from src.config import DEFAULT_DB_PATH


def get_connection(db_path=None):
    """
    Return a SQLite connection. Creates data directory if needed.
    """
    path = db_path or DEFAULT_DB_PATH
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(path)


def init_db(db_path=None):
    """
    Stub: create tables if they do not exist. Schema lives in models / migrations.
    """
    # TODO: Create assignments, study_sessions, user_preferences, etc. when models are defined.
    pass
