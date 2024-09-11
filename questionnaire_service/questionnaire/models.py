from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=355, blank=False, null=False)


class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


class FollowUpQuestion(models.Model):
    from_option = models.ForeignKey(Option, related_name='follow_ups', on_delete=models.CASCADE)
    from_question = models.ForeignKey(Question, related_name='follow_ups', on_delete=models.CASCADE)
    to_question = models.ForeignKey(Question, on_delete=models.CASCADE)


class TextAnswer(models.Model):
    question = models.ForeignKey(Question, related_name="text_answer", on_delete=models.CASCADE)
    answer_text = models.TextField(blank=False, null=False)


class MultiSelectOption(models.Model):
    question = models.ForeignKey(Question, related_name='multi_select_options', on_delete=models.CASCADE)
