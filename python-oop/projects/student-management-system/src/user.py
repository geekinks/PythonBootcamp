"""
User Subsystem: Abstract Base User Identity
"""
from abc import ABC, abstractmethod
import re


class User(ABC):
    """
    Abstract base class representing an authorized person within the institution.
    Encapsulates core identity, contact details, and notification capabilities.
    """

    def __init__(self, name: str, email: str, user_id: str):
        self._name = name.strip()
        self.email = email  # routes through property setter for validation
        self._user_id = user_id.strip()

    @property
    def name(self) -> str:
        """Read-only access to user's full name."""
        return self._name

    @property
    def user_id(self) -> str:
        """Read-only access to unique user identifier."""
        return self._user_id

    @property
    def email(self) -> str:
        """User email address."""
        return self._email

    @email.setter
    def email(self, value: str):
        """Validates and updates email address."""
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, value):
            raise ValueError(f"Invalid email address format: '{value}'")
        self._email = value.strip().lower()

    @abstractmethod
    def display_profile(self) -> str:
        """Abstract contract for rendering a user's role profile."""
        pass

    def send_notification(self, message: str) -> str:
        """Standard notification dispatch across all user types."""
        return f"[ALERT to {self.email}]: {message}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id='{self._user_id}' name='{self._name}'>"
