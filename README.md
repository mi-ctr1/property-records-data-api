# Pokemon Properties Data API

A lightweight REST-style API for storing and retrieving structured property record data. Built with Python, SQLite, and Flask.

## Overview

This project simulates a property records backend for a fictional property management company by the name of Pokemon Properties (named by my 6 year old son). It demonstrates relational database design, Python and SQL integration, and REST-style endpoint architecture.

**Stack:** Python · SQLite · Flask

## Database Schema

Four related tables connected by `property_id`:

| Table | Description |
|---|---|
| `properties` | Core property details: address, type, size, status |
| `owners` | Ownership records linked to each property |
| `valuations` | Market value history over time |
| `assessments` | Tax assessment data by year |

## Endpoints

### Properties

| Method | Endpoint | Description |
|---|---|---|
| GET | `/properties` | Returns all properties |
| GET | `/properties/<id>` | Returns a single property by ID |
| GET | `/properties?status=For Sale` | Filters by status |

### Owners

| Method | Endpoint | Description |
|---|---|---|
| GET | `/properties/<id>/owner` | Returns the owner record for a property |

### Valuations

| Method | Endpoint | Description |
|---|---|---|
| GET | `/properties/<id>/valuations` | Returns full valuation history for a property |

### Assessments

| Method | Endpoint | Description |
|---|---|---|
| GET | `/properties/<id>/assessment` | Returns the assessment for a property |
| GET | `/properties/<id>/assessment?year=2024` | Returns the assessment for a specific tax year |

### Full Record

| Method | Endpoint | Description |
|---|---|---|
| GET | `/properties/<id>/full` | Returns complete record — property, owner, valuations, and assessment |

## Project Structure

```
property-records-data-api/
├── database.py            # Schema creation and seed data
├── api.py                 # Query functions
├── app.py                 # Flask routes
├── main.py                # Test runner
├── requirements.txt       # Project dependencies
└── pokemonproperties.db   # SQLite database (auto-generated)
```
## Example Output

```
==================================================
 POKEMON PROPERTIES PROPERTY RECORDS API — TEST RUN
==================================================

[SETUP] Initializing database...
Tables created.
Sample data seeded.
Pokemon Properties database ready.

[TEST 1] Get all properties:
[
  {
    "id": 1,
    "address": "100 Pikachu Lane",
    "property_type": "Single Family",
    "bedrooms": 3,
    "bathrooms": 2.0,
    "square_feet": 1450,
    "status": "For Sale"
  },
  {
    "id": 2,
    "address": "102 Squirtle Street",
    "property_type": "Condo",
    "bedrooms": 2,
    "bathrooms": 1.0,
    "square_feet": 890,
    "status": "For Sale"
  },
  {
    "id": 3,
    "address": "104 Balbasaur Ave",
    "property_type": "Single Family",
    "bedrooms": 4,
    "bathrooms": 3.0,
    "square_feet": 2100,
    "status": "Sold"
  }
]

[TEST 2] Get property by ID (id=1):
{
  "id": 1,
  "address": "100 Pikachu Lane",
  "property_type": "Single Family",
  "bedrooms": 3,
  "bathrooms": 2.0,
  "square_feet": 1450,
  "status": "For Sale"
}

[TEST 3] Filter by status (For Sale):
[
  {
    "id": 1,
    "address": "100 Pikachu Lane",
    "property_type": "Single Family",
    "bedrooms": 3,
    "bathrooms": 2.0,
    "square_feet": 1450,
    "status": "For Sale"
  },
  {
    "id": 2,
    "address": "102 Squirtle Street",
    "property_type": "Condo",
    "bedrooms": 2,
    "bathrooms": 1.0,
    "square_feet": 890,
    "status": "For Sale"
  }
]

[TEST 4] Get owner for property id=3:
{
  "address": "104 Balbasaur Ave",
  "owner_name": "Priya Nair",
  "purchase_date": "2017-11-01"
}

[TEST 5] Get valuation history for property id=3:
[]

[TEST 6] Get assessment for property id=2, year=2024:
{
  "address": "102 Squirtle Street",
  "assessed_value": 158000,
  "land_value": 50000,
  "tax_year": 2024
}

[TEST 7] Get full record for property id=1:
{
  "property": {
    "id": 1,
    "address": "100 Pikachu Lane",
    "property_type": "Single Family",
    "bedrooms": 3,
    "bathrooms": 2.0,
    "square_feet": 1450,
    "status": "For Sale"
  },
  "owner": {
    "address": "100 Pikachu Lane",
    "owner_name": "Sandra Cole",
    "purchase_date": "2019-06-15"
  },
  "valuations": [
    {
      "address": "100 Pikachu Lane",
      "market_value": 270000,
      "valuation_date": "2022-01-01"
    },
    {
      "address": "100 Pikachu Lane",
      "market_value": 285000,
      "valuation_date": "2024-01-01"
    }
  ],
  "assessment": {
    "address": "100 Pikachu Lane",
    "assessed_value": 255000,
    "land_value": 80000,
    "tax_year": 2024
  }
}

[TEST 8] Get property that doesn't exist (id=999):
{
  "error": "No property found with id 999"
}

==================================================
 ALL TESTS COMPLETE
==================================================
```
## Planned Improvements

This project is designed to grow into a more robust utility. Potential improvements include:

### Post End-points
Adding new properties, owners, and assessments through the API rather than seed data only

### Input Validation
Ability to reject malformed or incomplete data before it reaches the database

### Error Handling
Consistent, structured error responses across all endpoints

### Authentication
Protect write endpoints so only authorized users can add or modify records