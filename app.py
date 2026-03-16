from flask import Flask, jsonify, request
from api import (
    get_all_properties,
    get_property_by_id,
    filter_by_status,
    get_owner_by_property,
    get_valuation_history,
    get_assessment,
    get_full_property_record,
)

app = Flask(__name__)


# ---------------------------------------------------------------------------
# PROPERTIES
# ---------------------------------------------------------------------------

@app.route("/properties", methods=["GET"])
def properties():
    """
    GET /properties
    GET /properties?status=For Sale
    """
    if request.args.get("status"):
        return jsonify(filter_by_status(request.args.get("status")))

    return jsonify(get_all_properties())


@app.route("/properties/<int:property_id>", methods=["GET"])
def property_by_id(property_id):
    """
    GET /properties/1
    """
    return jsonify(get_property_by_id(property_id))


# ---------------------------------------------------------------------------
# OWNERS
# ---------------------------------------------------------------------------

@app.route("/properties/<int:property_id>/owner", methods=["GET"])
def owner(property_id):
    """
    GET /properties/1/owner
    """
    return jsonify(get_owner_by_property(property_id))


# ---------------------------------------------------------------------------
# VALUATIONS
# ---------------------------------------------------------------------------

@app.route("/properties/<int:property_id>/valuations", methods=["GET"])
def valuations(property_id):
    """
    GET /properties/1/valuations
    """
    return jsonify(get_valuation_history(property_id))


# ---------------------------------------------------------------------------
# ASSESSMENTS
# ---------------------------------------------------------------------------

@app.route("/properties/<int:property_id>/assessment", methods=["GET"])
def assessment(property_id):
    """
    GET /properties/1/assessment?year=2024
    """
    year = request.args.get("year", 2024, type=int)
    return jsonify(get_assessment(property_id, year))


# ---------------------------------------------------------------------------
# FULL RECORD
# ---------------------------------------------------------------------------

@app.route("/properties/<int:property_id>/full", methods=["GET"])
def full_record(property_id):
    """
    GET /properties/1/full
    """
    return jsonify(get_full_property_record(property_id))


# ---------------------------------------------------------------------------
# RUN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
