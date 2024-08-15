"""
Django command to wait for the DB to be active.
"""


from typing import Any
from django.core.management.base import BaseCommand

print("HEllo")
class Command(BaseCommand):
    """Django command to wait for DB."""

    def handle(self, *args: Any, **options: Any) :
        pass