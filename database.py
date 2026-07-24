import sqlite3
from datetime import datetime


DB_NAME = "resume_history.db"


def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            created_at TEXT,

            ats_score INTEGER,

            job_match INTEGER,

            summary TEXT
        )
    """)

    conn.commit()

    conn.close()


def save_analysis(result):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history(
            created_at,
            ats_score,
            job_match,
            summary
        )
        VALUES(?,?,?,?)
        """,
        (
            datetime.now().strftime("%d-%m-%Y %H:%M"),
            result.get("ats_score", 0),
            result.get("job_match", 0),
            result.get("summary", "")
        )
    )

    conn.commit()

    conn.close()


def get_history():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

        id,

        created_at,

        ats_score,

        job_match

        FROM history

        ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data
