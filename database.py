import sqlite3

DB_NAME = "pokemonproperties.db"  # DB = database, DB_NAME = database_name


def get_connection():
    """Returns a connection to the Pokemon Properties database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Returns rows as dictionaries
    return conn


def create_tables():
    """Creates all tables if they don't already exist."""
    conn = get_connection()
    cursor = conn.cursor()

    # Core property record
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS properties (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            address         TEXT NOT NULL,
            property_type   TEXT NOT NULL,
            bedrooms        INTEGER,
            bathrooms       REAL,
            square_feet     INTEGER,
            status          TEXT NOT NULL
        )
    """)

    # Ownership records — linked to a property by property_id
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS owners (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id     INTEGER NOT NULL,
            owner_name      TEXT NOT NULL,
            purchase_date   TEXT,
            FOREIGN KEY (property_id) REFERENCES properties(id)
        )
    """)

    # Market valuation history — multiple valuations per property over time
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS valuations (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id     INTEGER NOT NULL,
            market_value    INTEGER NOT NULL,
            valuation_date  TEXT NOT NULL,
            FOREIGN KEY (property_id) REFERENCES properties(id)
        )
    """)

    # Tax assessment records — assessed value, land value, tax year
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id     INTEGER NOT NULL,
            assessed_value  INTEGER NOT NULL,
            land_value      INTEGER NOT NULL,
            tax_year        INTEGER NOT NULL,
            FOREIGN KEY (property_id) REFERENCES properties(id)
        )
    """)

    conn.commit()
    conn.close()
    print("Tables created.")


def seed_data():
    """Inserts sample data across all four tables."""
    conn = get_connection()
    cursor = conn.cursor()

    # --- Properties ---
    properties = [
        ("100 Pikachu Lane", "Single Family", 3, 2.0, 1450, "For Sale"),
        ("102 Squirtle Street", "Condo", 2, 1.0,  890, "For Sale"),
        ("104 Balbasaur Ave", "Single Family", 4, 3.0, 2100, "Sold"),
    ]

    cursor.executemany("""
        INSERT INTO properties
            (address, property_type, bedrooms, bathrooms, square_feet, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, properties)

    # --- Owners (one per property, property_id matches insertion order) ---
    owners = [
        (1,  "Sandra Cole", "2019-06-15"),
        (2,  "James Whitfield", "2021-03-22"),
        (3,  "Priya Nair", "2017-11-01"),
    ]

    cursor.executemany("""
        INSERT INTO owners (property_id, owner_name, purchase_date)
        VALUES (?, ?, ?)
    """, owners)

    # --- Valuations (two per property — shows value over time) ---
    valuations = [
        (1, 270000, "2022-01-01"), (1, 285000, "2024-01-01"),
        (2, 160000, "2022-01-01"), (2, 175000, "2024-01-01"),
        (3, 380000, "2022-01-01"), (3, 410000, "2024-01-01"),
    ]

    cursor.executemany("""
        INSERT INTO valuations (property_id, market_value, valuation_date)
        VALUES (?, ?, ?)
    """, valuations)

    # --- Assessments (one per property per tax year) ---
    assessments = [
        (1,  255000,  80000, 2024),
        (2,  158000,  50000, 2024),
        (3,  390000, 110000, 2024),
    ]

    cursor.executemany("""
        INSERT INTO assessments (property_id, assessed_value, land_value,
        tax_year)
        VALUES (?, ?, ?, ?)
    """, assessments)

    conn.commit()
    conn.close()
    print("Sample data seeded.")


def initialize_database():
    """Runs full setup: creates tables and seeds data."""
    create_tables()
    seed_data()
    print("Maplewood database ready.")


if __name__ == "__main__":
    initialize_database()
