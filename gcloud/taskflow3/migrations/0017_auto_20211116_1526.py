# Generated by Django 2.2.24 on 2021-11-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskflow3", "0016_merge_20210519_1911"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskflowinstance",
            name="create_method",
            field=models.CharField(
                choices=[
                    ("app", "手动"),
                    ("api", "API网关"),
                    ("app_maker", "轻应用"),
                    ("periodic", "周期任务"),
                    ("clocked", "计划任务"),
                    ("mobile", "移动端"),
                ],
                default="app",
                max_length=30,
                verbose_name="创建方式",
            ),
        ),
        migrations.CreateModel(
            name="AutoRetryNodeStrategy",
            fields=[
                ("taskflow_id", models.BigIntegerField(verbose_name="taskflow id")),
                ("root_pipeline_id", models.CharField(max_length=64, verbose_name="root pipeline id")),
                (
                    "node_id",
                    models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name="task node id"),
                ),
                ("retry_times", models.IntegerField(default=0, verbose_name="retry times")),
                ("max_retry_times", models.IntegerField(default=5, verbose_name="retry times")),
            ],
            options={"index_together": {("root_pipeline_id", "node_id")},},
        ),
    ]