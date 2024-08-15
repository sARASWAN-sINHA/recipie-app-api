"""
Django command to wait for the DB to be active.
"""


from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for DB."""

    def handle(self, *args: Any, **options: Any) -> str | None:
        pass