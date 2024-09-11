from django.contrib import admin
from .models import Question, Option, FollowUpQuestion, TextAnswer, MultiSelectOption
# Register your models here.

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(FollowUpQuestion)
admin.site.register(TextAnswer)
admin.site.register(MultiSelectOption)
