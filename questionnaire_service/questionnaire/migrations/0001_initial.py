# Generated by Django 4.2.3 on 2024-05-31 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=355)),
            ],
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_answer', to='questionnaire.question')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='questionnaire.question')),
            ],
        ),
        migrations.CreateModel(
            name='MultiSelectOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multi_select_options', to='questionnaire.question')),
            ],
        ),
        migrations.CreateModel(
            name='FollowUpQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_ups', to='questionnaire.option')),
                ('from_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_ups', to='questionnaire.question')),
                ('to_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.question')),
            ],
        ),
    ]
