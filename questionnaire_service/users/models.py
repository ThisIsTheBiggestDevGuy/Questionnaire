from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from questionnaire.models import Question

# Models here:


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Thread(models.Model):
    user = models.ForeignKey(User, related_name='threads', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    questions = models.ManyToManyField(Question)
    is_public = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('thread-detail', kwargs={'slug': self.slug})


class Response(models.Model):
    thread = models.ForeignKey(Thread, related_name='responses', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)
    selected_options = models.ManyToManyField('questionnaire.Option', blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

