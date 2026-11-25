import duckdb

con = duckdb.connect("website_sessions.duckdb")

con.execute("""
CREATE TABLE website_sessions (
    session_id INTEGER,
    user_id INTEGER,
    timestamp TIMESTAMP
)
""")

con.execute("""
INSERT INTO website_sessions VALUES
""")

con.close()
