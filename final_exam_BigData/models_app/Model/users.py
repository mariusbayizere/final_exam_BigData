"""
This file contains the Django model User which is used to store
information about users in the database.
"""


from django.db import models


class User(models.Model):
    """
    A Django model representing a User with various attributes.
    """
    username = models.CharField(max_length=255, unique=True)
    """The username of the user."""
    password_hash = models.CharField(max_length=255)
    """The password hash of the user."""
    role = models.CharField(max_length=10, choices=[
        ('admin', 'admin'),
        ('user', 'user')
    ])
    """The role of the user; can be 'admin' or 'user'."""
    created_at = models.DateTimeField(auto_now_add=True)
    """The timestamp when the user was created."""


    class Meta:
        db_table = 'Users'

    def __str__(self):
        """
        Returns the string representation of the User object, which is the
        username.
        """
        return self.username