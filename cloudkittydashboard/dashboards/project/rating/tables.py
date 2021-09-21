# Copyright 2018 Objectif Libre
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from django.utils.translation import ugettext_lazy as _
from dashboards.admin.summary.tables import TotalColumn
from horizon import tables


class SummaryTable(tables.DataTable):
    """This table formats a summary for the given tenant."""

    res_type = tables.Column('res_type', verbose_name=_('Metric Type'))
    rate = TotalColumn('rate', verbose_name=_('Rate'))

    class Meta(object):
        name = "summary"
        verbose_name = _("Summary")
