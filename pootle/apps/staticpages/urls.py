#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012-2013 Zuza Software Foundation
#
# This file is part of Pootle.
#
# Pootle is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# translate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with translate; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from django.conf.urls import patterns, url

from .views import AdminTemplateView, PageCreateView, PageUpdateView

urlpatterns = patterns('',
    url(r'^(?P<virtual_path>.+)/$',
        'staticpages.views.display_page',
        name='staticpages.display'),
)

admin_patterns = patterns('',
    url(r'^$',
        AdminTemplateView.as_view(),
        name='staticpages.admin'),

    url(r'^(?P<page_type>[^/]+)/add/?$',
        PageCreateView.as_view(),
        name='staticpages.create'),
    url(r'^(?P<page_type>[^/]+)/(?P<pk>\d+)/?$',
        PageUpdateView.as_view(),
        name='staticpages.edit'),
)
