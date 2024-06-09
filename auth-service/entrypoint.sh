#!/usr/bin/env bash
# Seed the database with admin credentials
python seed_db.py

# Run the application
exec "$@"
