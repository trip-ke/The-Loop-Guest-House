from django.conf import settings
from django.db import models


class HousekeepingTask(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "To Do"
        IN_PROGRESS = "in_progress", "In Progress"
        DONE = "done", "Done"
        BLOCKED = "blocked", "Blocked"

    room = models.ForeignKey("rooms.Room", on_delete=models.PROTECT, related_name="housekeeping_tasks")
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="housekeeping_tasks",
    )
    title = models.CharField(max_length=120)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)
    due_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["status", "due_date", "room__number"]

    def __str__(self):
        return f"{self.title} - {self.room}"

# Create your models here.
