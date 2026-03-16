from database import get_connection


# ---------------------------------------------------------------------------
# PROPERTIES
# ---------------------------------------------------------------------------

def get_property_by_id(property_id):
    """
    Returns a single property record by its ID.
    REST equivalent: GET /properties/<id>
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM properties
        WHERE id = ?
    """, (property_id,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return {"error": f"No property found with id {property_id}"}

    return dict(row)


def get_all_properties():
    """
    Returns all property records.
    REST equivalent: GET /properties
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM properties")

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


def filter_by_status(status):
    """
    Returns all properties matching a given status.
    Status options: 'For Sale', 'For Rent', 'Sold'
    REST equivalent: GET /properties?status=For Sale
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM properties
        WHERE status = ?
    """, (status,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


# ---------------------------------------------------------------------------
# OWNERS
# ---------------------------------------------------------------------------

def get_owner_by_property(property_id):
    """
    Returns the owner record for a given property.
    Uses a JOIN to combine property address with owner details.
    REST equivalent: GET /properties/<id>/owner
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            properties.address,
            owners.owner_name,
            owners.purchase_date
        FROM properties
        JOIN owners ON properties.id = owners.property_id
        WHERE properties.id = ?
    """, (property_id,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return {"error": f"No owner found for property id {property_id}"}

    return dict(row)


# ---------------------------------------------------------------------------
# VALUATIONS
# ---------------------------------------------------------------------------

def get_valuation_history(property_id):
    """
    Returns all market valuations for a property over time.
    REST equivalent: GET /properties/<id>/valuations
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            properties.address,
            valuations.market_value,
            valuations.valuation_date
        FROM properties
        JOIN valuations ON properties.id = valuations.property_id
        WHERE properties.id = ?
        ORDER BY valuations.valuation_date ASC
    """, (property_id,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


# ---------------------------------------------------------------------------
# ASSESSMENTS
# ---------------------------------------------------------------------------

def get_assessment(property_id, tax_year):
    """
    Returns the tax assessment for a property in a given year.
    REST equivalent: GET /properties/<id>/assessment?year=2024
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            properties.address,
            assessments.assessed_value,
            assessments.land_value,
            assessments.tax_year
        FROM properties
        JOIN assessments ON properties.id = assessments.property_id
        WHERE properties.id = ?
        AND assessments.tax_year = ?
    """, (property_id, tax_year))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return {"error": f"No assessment found for property {property_id}"
                         f"in {tax_year}"}

    return dict(row)


# ---------------------------------------------------------------------------
# FULL RECORD
# ---------------------------------------------------------------------------

def get_full_property_record(property_id):
    """
    Returns a complete record for a property:
    property details + owner + latest valuation + latest assessment.
    REST equivalent: GET /properties/<id>/full
    """
    property_data = get_property_by_id(property_id)
    if "error" in property_data:
        return property_data

    owner_data = get_owner_by_property(property_id)
    valuation_history = get_valuation_history(property_id)
    assessment_data = get_assessment(property_id, 2024)

    return {
        "property":   property_data,
        "owner":      owner_data,
        "valuations": valuation_history,
        "assessment": assessment_data,
    }
