import os

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver


class Task(models.Model):
    """Task Model"""

    owner = models.ManyToManyField(User, verbose_name="owner")
    name = models.CharField("name", max_length=20)
    description = models.CharField("description", max_length=100)
    deadline = models.DateTimeField("deadline")
    picture = models.ImageField("picture", upload_to="task_pics/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


@receiver(models.signals.post_delete, sender=Task)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)


@receiver(models.signals.pre_save, sender=Task)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Task.objects.get(pk=instance.pk).picture
    except Task.DoesNotExist:
        return False

    new_file = instance.picture
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
