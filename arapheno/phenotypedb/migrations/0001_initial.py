# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('sitename', models.TextField(blank=True, null=True)),
                ('collector', models.TextField(blank=True, null=True)),
                ('collection_date', models.DateTimeField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, db_index=True, null=True)),
                ('latitude', models.FloatField(blank=True, db_index=True, null=True)),
                ('cs_number', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ObservationUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenotypedb.Accession')),
            ],
        ),
        migrations.CreateModel(
            name='OntologySource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='OntologyTerm',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('definition', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenotypedb.OntologySource')),
            ],
        ),
        migrations.CreateModel(
            name='Phenotype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('scoring', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('growth_conditions', models.TextField(blank=True, null=True)),
                ('shapiro_test_statistic', models.FloatField(blank=True, null=True)),
                ('shapiro_p_value', models.FloatField(blank=True, null=True)),
                ('number_replicates', models.IntegerField(default=0)),
                ('integration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhenotypeMetaDynamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phenotype_meta_field', models.CharField(db_index=True, max_length=255)),
                ('phenotype_meta_value', models.TextField()),
                ('phenotype_public', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phenotypedb.Phenotype')),
            ],
        ),
        migrations.CreateModel(
            name='PhenotypeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('obs_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenotypedb.ObservationUnit')),
                ('phenotype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenotypedb.Phenotype')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_order', models.TextField()),
                ('publication_tag', models.CharField(max_length=255)),
                ('pub_year', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('journal', models.CharField(max_length=255)),
                ('volume', models.CharField(blank=True, max_length=255, null=True)),
                ('pages', models.CharField(blank=True, max_length=255, null=True)),
                ('doi', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('pubmed_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('authors', models.ManyToManyField(to='phenotypedb.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ncbi_id', models.IntegerField(blank=True, null=True)),
                ('genus', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('publications', models.ManyToManyField(blank=True, to='phenotypedb.Publication')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenotypedb.Species')),
            ],
        ),
        migrations.AddField(
            model_name='phenotype',
            name='dynamic_metainformations',
            field=models.ManyToManyField(to='phenotypedb.PhenotypeMetaDynamic'),
        ),
        migrations.AddField(
            model_name='phenotype',
            name='eo_term',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eo_term', to='phenotypedb.OntologyTerm'),
        ),
        migrations.AddField(
            model_name='phenotype',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenotypedb.Species'),
        ),
        migrations.AddField(
            model_name='phenotype',
            name='study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenotypedb.Study'),
        ),
        migrations.AddField(
            model_name='phenotype',
            name='to_term',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_term', to='phenotypedb.OntologyTerm'),
        ),
        migrations.AddField(
            model_name='phenotype',
            name='uo_term',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uo_term', to='phenotypedb.OntologyTerm'),
        ),
        migrations.AddField(
            model_name='observationunit',
            name='study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenotypedb.Study'),
        ),
        migrations.AddField(
            model_name='accession',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phenotypedb.Species'),
        ),
    ]
