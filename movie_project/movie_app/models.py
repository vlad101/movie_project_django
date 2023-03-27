from django.db import models

class OMDBMovieKey(models.Model):
    """
    Model for holding information about OMDB movie keys.
    """
    # An auto-incremented primary key ID field
    id = models.AutoField(primary_key=True)
    # A string key field with a maximum length of 30 characters
    key = models.CharField(max_length=30, unique=True)
    # A boolean field to store the valid value, set to True by default
    is_valid = models.BooleanField(default=True)
    # A DateTime field to store the timestamp of when the key was created
    created_at = models.DateTimeField(auto_now_add=True)
    # A DateTime field to store the timestamp of when the key was last updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Set the default ordering for the model to be by the timestamp of when the key was created
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of the OMDB movie key.
        """
        return f'OMDBMovieKey: {self.key} ({self.is_valid})'