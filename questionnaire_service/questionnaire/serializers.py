from rest_framework import serializers
from .models import Question, Option, FollowUpQuestion, TextAnswer, MultiSelectOption


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text']


class FollowUpQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUpQuestion
        fields = ['id', 'from_option', 'from_question', 'to_question']


class TextAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextAnswer
        fields = ['id', 'answer_text']


class MultiSelectOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiSelectOption
        fields = ['id', 'option_text']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    follow_ups = FollowUpQuestionSerializer(many=True, read_only=True)
    text_answers = TextAnswerSerializer(many=True, read_only=True)
    multi_select_options = MultiSelectOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'options', 'follow_ups','text_answers', 'multi_select_options']
