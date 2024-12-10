import os
import sqlite3
import pandas as pd
import subprocess

# Define paths and constants
DATA_DIR = "../data"
GDP_CSV = os.path.join(DATA_DIR, "gdp_cleaned.csv")
EDU_CSV = os.path.join(DATA_DIR, "edu_cleaned.csv")
SQLITE_DB = os.path.join(DATA_DIR, "data_cleaned.db")
PIPELINE_SCRIPT = "./project/pipeline.py"


def test_pipeline_execution():
    """
    Test if the pipeline script executes successfully.
    """
    print("Testing pipeline execution...")
    result = subprocess.run(["python", PIPELINE_SCRIPT], capture_output=True, text=True)
    assert result.returncode == 0, f"Pipeline script failed: {result.stderr}"
    print("Pipeline executed successfully.")


def test_gdp_csv_exists():
    """
    Test if the GDP cleaned CSV file is created.
    """
    print("Testing if GDP cleaned CSV exists...")
    assert os.path.exists(GDP_CSV), f"GDP cleaned CSV file not found: {GDP_CSV}"
    print("GDP cleaned CSV exists.")


def test_edu_csv_exists():
    """
    Test if the Education cleaned CSV file is created.
    """
    print("Testing if Education cleaned CSV exists...")
    assert os.path.exists(EDU_CSV), f"Education cleaned CSV file not found: {EDU_CSV}"
    print("Education cleaned CSV exists.")


def test_gdp_csv_content():
    """
    Test the content of the GDP cleaned CSV file.
    """
    print("Testing GDP cleaned CSV content")
    df = pd.read_csv(GDP_CSV)
    assert not df.empty, "GDP cleaned CSV file is empty."
    assert "Country Name" in df.columns, "Expected column 'Country Name' not found in GDP CSV."
    assert "Year" in df.columns, "Expected column 'Year' not found in GDP CSV."
    print("GDP cleaned CSV content is valid.")


def test_edu_csv_content():
    """
    Test the content of the Education cleaned CSV file.
    """
    print("Testing Education cleaned CSV content.")
    df = pd.read_csv(EDU_CSV)
    assert not df.empty, "Education cleaned CSV file is empty."
    assert "Country Name" in df.columns, "Expected column 'Country Name' not found in Education CSV."
    assert "Year" in df.columns, "Expected column 'Year' not found in Education CSV."
    print("Education cleaned CSV content is valid.")


def test_sqlite_db_exists():
    """
    Test if the SQLite database file is created.
    """
    print("Testing if SQLite database exists..")
    assert os.path.exists(SQLITE_DB), f"SQLite database not found: {SQLITE_DB}"
    print("SQLite database exists.")


def test_sqlite_tables():
    """
    Test if the expected tables exist in the SQLite database.
    """
    print("Testing SQLite database tables.")
    with sqlite3.connect(SQLITE_DB) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        assert "gdp_data" in tables, "Table 'gdp_data' not found in SQLite database."
        assert "education_data" in tables, "Table 'education_data' not found in SQLite database."
        print("Expected tables found in SQLite database.")


def test_sqlite_table_content():
    """
    Test the content of the tables in the SQLite database.
    """
    print("Testing SQLite database table content...")
    with sqlite3.connect(SQLITE_DB) as conn:
        gdp_df = pd.read_sql("SELECT * FROM gdp_data;", conn)
        edu_df = pd.read_sql("SELECT * FROM education_data;", conn)
        assert not gdp_df.empty, "Table 'gdp_data' in SQLite database is empty."
        assert not edu_df.empty, "Table 'education_data' in SQLite database is empty."
        print("SQLite database tables contain valid data.")


if __name__ == "__main__":
    # Run all tests accordinglz
    test_pipeline_execution()
    test_gdp_csv_exists()
    test_edu_csv_exists()
    test_gdp_csv_content()
    test_edu_csv_content()
    test_sqlite_db_exists()
    test_sqlite_tables()
    test_sqlite_table_content()

    print("All tests passed successfullz.")
