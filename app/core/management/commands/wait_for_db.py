"""
Django command to wait for the DB to be active.
"""

import time
from typing import Any
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2.errors import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """Django command to wait for DB."""

    def handle(self, *args: Any, **options: Any):
        """Entry point for command."""
        db_up = False
        self.stdout.write("\nWaiting for database...")

        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(
                    "Database connection failed!! \
                    Waiting for 1 sec..."
                )
                time.sleep(1)
        self.stdout.write(
            self.style.SUCCESS("Database connection established!")
        )
