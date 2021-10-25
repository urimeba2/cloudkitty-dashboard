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

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.http import urlencode

from horizon import tables


def get_details_link(datum):
    if datum.tenant_id:
        url = "horizon:admin:rating_summary:project_details"
        return reverse(url, kwargs={'project_id': datum.tenant_id})

class TotalColumn(tables.Column):
    def get_data(self, datum):
        return '$ {rate} USD'.format(rate=datum.rate)

class CreateMethodPayment(tables.LinkAction):
    name = "create"
    verbose_name = "Create Method Payment"
    url = "horizon:admin:flavors:create"
    classes = ("ajax-modal",)
    policy_rules = (("identity", "admin_required"),)
    icon = "plus"


class ModifyMethodPayment(tables.LinkAction):
    name = "methods"
    verbose_name = "Modify Method"
    url = "horizon:admin:flavors:update"
    classes = ("ajax-modal",)
    # policy_rules = (("identity", "admin_required"),)
    icon = "pencil"

    def get_link_url(self, flavor):
        step = 'update_flavor_access'
        base_url = reverse(self.url, args=[flavor.id])
        param = urlencode({"step": step})
        return "?".join([base_url, param])

    # def allowed(self, request, flavor=None):
    #     return not flavor.is_public

class SummaryTable(tables.DataTable):
    project_id = tables.Column('tenant_id', verbose_name="Project ID2", link=get_details_link)
    project_name = tables.Column('name', verbose_name="Project Name2", link=get_details_link)
    total = TotalColumn('rate', verbose_name="Project Total2")

    class Meta(object):
        name = "payments"
        verbose_name = "Payments"
        table_actions = (CreateMethodPayment,)
        row_actions = (ModifyMethodPayment,)


class TenantSummaryTable(tables.DataTable):
    res_type = tables.Column('res_type', verbose_name=_("Res Type"))
    rate = TotalColumn('rate', verbose_name=_("Rate"))

    class Meta(object):
        name = "tenant_summary"
        verbose_name = _("Tenant Summary")
