import json
from database import initialize_database
from api import (
    get_all_properties,
    get_property_by_id,
    filter_by_status,
    get_owner_by_property,
    get_valuation_history,
    get_assessment,
    get_full_property_record,
)


def pretty(data):
    """Prints data as formatted JSON so it's easy to read."""
    print(json.dumps(data, indent=2))


def run_tests():

    print("\n" + "="*50)
    print(" POKEMON PROPERTIES PROPERTY RECORDS API — TEST RUN")
    print("="*50)

    # --- Setup ---
    print("\n[SETUP] Initializing database...")
    initialize_database()

    # --- All Properties ---
    print("\n[TEST 1] Get all properties:")
    pretty(get_all_properties())

    # --- Single Property ---
    print("\n[TEST 2] Get property by ID (id=1):")
    pretty(get_property_by_id(1))

    # --- Filter by Status ---
    print("\n[TEST 3] Filter by status (For Sale):")
    pretty(filter_by_status("For Sale"))

    # --- Owner ---
    print("\n[TEST 4] Get owner for property id=3:")
    pretty(get_owner_by_property(3))

    # --- Valuation History ---
    print("\n[TEST 5] Get valuation history for property id=3:")
    pretty(get_valuation_history(5))

    # --- Assessment ---
    print("\n[TEST 6] Get assessment for property id=2, year=2024:")
    pretty(get_assessment(2, 2024))

    # --- Full Record ---
    print("\n[TEST 7] Get full record for property id=1:")
    pretty(get_full_property_record(1))

    # --- Edge Case: Property not found ---
    print("\n[TEST 8] Get property that doesn't exist (id=999):")
    pretty(get_property_by_id(999))

    print("\n" + "="*50)
    print(" ALL TESTS COMPLETE")
    print("="*50 + "\n")


if __name__ == "__main__":
    run_tests()
