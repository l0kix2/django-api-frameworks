# coding: utf-8
from __future__ import unicode_literals

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.resources import Resource
from tastypie import fields

from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()

#        filtering = {
#            'username': ALL,
#            'date_joined': ALL,
#        }

    def build_filters(self, filters=None):
        orm_filters = super(UserResource, self).build_filters(filters)

        if filters is None:
            filters = {}

        if 'username' in filters:
            orm_filters['username'] = 'admin'

        return orm_filters

class LogUserResource(ModelResource):
    shmuser = fields.ToOneField(UserResource, 'user', full=True)
    class Meta:
        queryset = LogEntry.objects.all()
        filtering = {
            'shmuser': ALL_WITH_RELATIONS,
        }


class UserLogsResource(ModelResource):
    logs = fields.ToManyField(LogUserResource, 'logentry_set', full=True)
    class Meta:
        queryset = User.objects.all()


class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()

class UserGroupResource(ModelResource):
    groups = fields.ToManyField(GroupResource, 'groups', full=True)
    class Meta:
        queryset = User.objects.all()
