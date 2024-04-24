# Generated by Django 5.0.3 on 2024-04-24 15:59

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street1', models.TextField(max_length=30)),
                ('street2', models.TextField(max_length=30, null=True)),
                ('city', models.TextField(max_length=30)),
                ('state', models.TextField(max_length=2)),
                ('postal', models.TextField(max_length=20)),
                ('country', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.address')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=30)),
                ('intake_type', models.CharField(blank=True, choices=[('C', 'Captured in wild'), ('S', 'Surrendered by previous owner')], max_length=1)),
                ('intake_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.CharField(max_length=300)),
                ('age', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('ready_to_adopt', models.BooleanField()),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('timeStamp', models.TimeField(default=django.utils.timezone.now)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.person')),
            ],
        ),
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.person')),
                ('can_adopt', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('core.person',),
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.animal')),
                ('is_fixed', models.BooleanField()),
                ('breed', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('core.animal',),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.animal')),
                ('is_fixed', models.BooleanField()),
                ('breed', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('core.animal',),
        ),
        migrations.CreateModel(
            name='Turtle',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.animal')),
                ('species', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('core.animal',),
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.address')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='shelter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.shelter'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField(default=datetime.datetime(2024, 5, 1, 15, 59, 59, 287222, tzinfo=datetime.timezone.utc))),
                ('completion_datetime', models.DateTimeField(blank=True, null=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('required_role', models.CharField(choices=[('MA', 'Manager'), ('RE', 'Regular'), ('VT', 'Veterenarian'), ('NA', 'Any Role')], max_length=2)),
                ('is_released', models.BooleanField(default=False)),
                ('animal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.animal')),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.shelter')),
            ],
        ),
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.IntegerField()),
                ('text', models.TextField()),
                ('is_complete', models.BooleanField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.person')),
                ('start_date', models.DateField()),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.shelter')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('core.person',),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.person')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('MA', 'Manager'), ('RE', 'Regular'), ('VT', 'Veterenarian')], max_length=2)),
                ('hire_date', models.DateField()),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.shelter')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('core.person',),
        ),
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.worker'),
        ),
        migrations.CreateModel(
            name='AnimalComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.comment')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.animal')),
            ],
            bases=('core.comment',),
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.comment')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
            ],
            bases=('core.comment',),
        ),
    ]
