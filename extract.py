import duckdb

duckdb.sql("""
    COPY (
        SELECT DISTINCT
             TRIM(session_id) AS session_id,
             session_date,
             customer_id,
             store_id,
             TRIM(device_type) AS device_type,
             SPLIT_PART(TRIM(browser), '|', 1) AS browser,
             SPLIT_PART(TRIM(browser), '|', 2) AS os,
             session_purchase_made,
             session_duration_minutes,
             session_page_visited,
             COALESCE(session_quality_score, avg(session_quality_score) OVER()) AS session_quality_score
        FROM 'bronze_website_sessions.parquet'
    )
    TO 'silver_website_sessions.parquet' 
    (FORMAT PARQUET);
""")