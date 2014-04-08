# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Title.title_number'
        db.add_column(u'titles_title', 'title_number',
                      self.gf('django.db.models.fields.TextField')(default='1'),
                      keep_default=False)

        # Adding field 'Title.content'
        db.add_column(u'titles_title', 'content',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Title.title_number'
        db.delete_column(u'titles_title', 'title_number')

        # Deleting field 'Title.content'
        db.delete_column(u'titles_title', 'content')


    models = {
        u'titles.title': {
            'Meta': {'object_name': 'Title'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'extent': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title_number': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['titles']