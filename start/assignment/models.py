from django.db import models
from django.conf import settings
from django.urls import reverse

from django.conf import settings
from study.models import Group


class Assignment(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    index_in_group = models.IntegerField()
    title = models.CharField(max_length=30, verbose_name='과제명')
    content = models.TextField(verbose_name='내용')
    due_date = models.DateTimeField(verbose_name='기한')
    created_at = models.DateTimeField(auto_now_add=True)
    done_checked = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('assignment:assignment_detail', args=[self.id])

    def submitters(self):
        return [x.author for x in Done.objects.filter(assignment=self)]


class Done(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='dones')
    index_in_assignment = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    done_img = models.ImageField(upload_to='AssignmentsDone')
    injung = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('assignment:done_detail', args=[self.id])

    def injung_check(self):
        return [x.author for x in Injung_history.objects.filter(done=self)]

    def index_in_group(self):
        dones = [x for x in Done.objects.filter(assignment__group=self.assignment.group).order_by('created_at')]
        return dones.index(self)+1


class Injung_history(models.Model):
    done = models.ForeignKey(Done, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
