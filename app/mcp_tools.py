from app.db import get_connection

def query_policies(question: str) -> str:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.content
        FROM policies p
        WHERE p.content ILIKE %s
        LIMIT 3
    """, (f"%{question}%",))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    if not rows:
        return "No relevant policy found."

    return "\n\n".join(r[0] for r in rows)

