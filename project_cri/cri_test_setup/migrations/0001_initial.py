# Generated by Django 3.0.4 on 2020-04-10 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CriBranch',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=200, null=True)),
            ],
            options={
                'db_table': 'CRI_BRANCH',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CriBranchConfig',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('auto', models.IntegerField(db_column='AUTO')),
                ('s2c', models.IntegerField(db_column='S2C')),
                ('manual', models.IntegerField(db_column='MANUAL')),
                ('allowed_conflict_count', models.IntegerField(blank=True, db_column='ALLOWED_CONFLICT_COUNT', null=True)),
                ('allowed_build_duration', models.IntegerField(blank=True, db_column='ALLOWED_BUILD_DURATION', null=True)),
                ('allowed_iterations', models.IntegerField(blank=True, db_column='ALLOWED_ITERATIONS', null=True)),
                ('evo_project', models.CharField(blank=True, db_column='EVO_PROJECT', max_length=2000, null=True)),
                ('mirror_sites', models.CharField(blank=True, db_column='MIRROR_SITES', max_length=2000, null=True)),
                ('publish_root', models.CharField(blank=True, db_column='PUBLISH_ROOT', max_length=2000, null=True)),
                ('space_required', models.IntegerField(blank=True, db_column='SPACE_REQUIRED', null=True)),
                ('sb_create', models.CharField(blank=True, db_column='SB_CREATE', max_length=2000, null=True)),
                ('sb_pre_build', models.CharField(blank=True, db_column='SB_PRE_BUILD', max_length=2000, null=True)),
                ('sb_build', models.CharField(blank=True, db_column='SB_BUILD', max_length=2000, null=True)),
                ('sb_post_build', models.CharField(blank=True, db_column='SB_POST_BUILD', max_length=2000, null=True)),
                ('lastest_refinement_lg', models.CharField(blank=True, db_column='LASTEST_REFINEMENT_LG', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'CRI_BRANCH_CONFIG',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CriProject',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=100, unique=True)),
            ],
            options={
                'db_table': 'CRI_PROJECT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CriProjectConfig',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('jenkins_url', models.CharField(blank=True, db_column='JENKINS_URL', max_length=2000, null=True)),
                ('jenkins_user', models.CharField(blank=True, db_column='JENKINS_USER', max_length=2000, null=True)),
                ('jenkins_apitoken', models.CharField(blank=True, db_column='JENKINS_APITOKEN', max_length=2000, null=True)),
                ('jenkins_scheduler', models.CharField(blank=True, db_column='JENKINS_SCHEDULER', max_length=2000, null=True)),
                ('jenkins_controller', models.CharField(blank=True, db_column='JENKINS_CONTROLLER', max_length=2000, null=True)),
                ('jenkins_credential_id', models.CharField(blank=True, db_column='JENKINS_CREDENTIAL_ID', max_length=2000, null=True)),
                ('jenkins_node_label', models.CharField(blank=True, db_column='JENKINS_NODE_LABEL', max_length=2000, null=True)),
            ],
            options={
                'db_table': 'CRI_PROJECT_CONFIG',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CriRefinementState',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=20, unique=True)),
            ],
            options={
                'db_table': 'CRI_REFINEMENT_STATE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CriRefinementType',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=15, unique=True)),
            ],
            options={
                'db_table': 'CRI_REFINEMENT_TYPE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CriRequest',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('patch', models.CharField(blank=True, db_column='PATCH', max_length=200, null=True)),
                ('s2c_id', models.IntegerField(blank=True, db_column='S2C_ID', null=True)),
            ],
            options={
                'db_table': 'CRI_REQUEST',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CriServer',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=100, unique=True)),
                ('path', models.CharField(db_column='PATH', max_length=1000)),
            ],
            options={
                'db_table': 'CRI_SERVER',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CriStatus',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('refinement_iteration', models.IntegerField(blank=True, db_column='REFINEMENT_ITERATION', null=True)),
                ('jenkins_job_url', models.CharField(blank=True, db_column='JENKINS_JOB_URL', max_length=2000, null=True)),
                ('server', models.CharField(blank=True, db_column='SERVER', max_length=256, null=True)),
                ('sb_path', models.CharField(blank=True, db_column='SB_PATH', max_length=1000, null=True)),
                ('create_duration', models.IntegerField(blank=True, db_column='CREATE_DURATION', null=True)),
                ('patch_duration', models.IntegerField(db_column='PATCH_DURATION')),
                ('ea_build_url', models.CharField(blank=True, db_column='EA_BUILD_URL', max_length=2000, null=True)),
                ('conflicts', models.IntegerField(blank=True, db_column='CONFLICTS', null=True)),
                ('build_duration', models.IntegerField(blank=True, db_column='BUILD_DURATION', null=True)),
                ('patch_owner', models.CharField(blank=True, db_column='PATCH_OWNER', max_length=20, null=True)),
                ('notes', models.CharField(blank=True, db_column='NOTES', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'CRI_STATUS',
                'managed': False,
            },
        ),
    ]