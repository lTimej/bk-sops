# Generated by Django 3.2.12 on 2022-06-12 17:37

from django.db import migrations, models

from gcloud.constants import CLOCKED_TASK_NOT_STARTED, CLOCKED_TASK_STARTED


def reverse_func(apps, schema_editor):
    ClockedTask = apps.get_model("clocked_task", "ClockedTask")
    db_alias = schema_editor.connection.alias
    ClockedTask.objects.using(db_alias).all().update(state=CLOCKED_TASK_NOT_STARTED)


def forward_func(apps, schema_editor):
    ClockedTask = apps.get_model("clocked_task", "ClockedTask")
    ClockedTask.objects.exclude(task_id=None).update(state=CLOCKED_TASK_STARTED)


class Migration(migrations.Migration):

    dependencies = [
        ("clocked_task", "0004_auto_20220601_1602"),
    ]

    operations = [
        migrations.AddField(
            model_name="clockedtask",
            name="state",
            field=models.CharField(
                choices=[("not_started", "未执行"), ("started", "已执行"), ("start_failed", "启动失败")],
                default="not_started",
                help_text="计划任务状态",
                max_length=64,
            ),
        ),
        migrations.RunPython(forward_func, reverse_func),
    ]