from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Movie(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'))
    genre = models.CharField(_('genre'), max_length=50)
    movie_length = models.CharField(_('movie length'), max_length=50)
    user = models.ForeignKey(
        User,
        verbose_name="user",
        on_delete=models.CASCADE,
        related_name="movies"
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    def __str__(self):
        return _("{title} added by {user} at {created_at}").format(
            title=self.title,
            user=self.user,
            created_at=self.created_at
        )

    class Meta:
        ordering = ('-created_at', )


