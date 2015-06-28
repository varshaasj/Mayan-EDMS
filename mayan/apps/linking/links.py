from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from acls.permissions import acls_view_acl
from documents.permissions import permission_document_view
from navigation import Link

from .permissions import (
    permission_smart_link_create, permission_smart_link_delete,
    permission_smart_link_edit, permission_smart_link_view
)

link_smart_link_acl_list = Link(permissions=[acls_view_acl], text=_('ACLs'), view='linking:smart_link_acl_list', args='object.pk')
link_smart_link_condition_create = Link(permissions=[permission_smart_link_edit], text=_('create condition'), view='linking:smart_link_condition_create', args='object.pk')
link_smart_link_condition_delete = Link(permissions=[permission_smart_link_edit], tags='dangerous', text=_('delete'), view='linking:smart_link_condition_delete', args='resolved_object.pk')
link_smart_link_condition_edit = Link(permissions=[permission_smart_link_edit], text=_('edit'), view='linking:smart_link_condition_edit', args='resolved_object.pk')
link_smart_link_condition_list = Link(permissions=[permission_smart_link_edit], text=_('conditions'), view='linking:smart_link_condition_list', args='object.pk')
link_smart_link_create = Link(permissions=[permission_smart_link_create], text=_('create new smart link'), view='linking:smart_link_create')
link_smart_link_delete = Link(permissions=[permission_smart_link_delete], tags='dangerous', text=_('delete'), view='linking:smart_link_delete', args='object.pk')
link_smart_link_document_types = Link(permissions=[permission_smart_link_edit], text=_('document types'), view='linking:smart_link_document_types', args='object.pk')
link_smart_link_edit = Link(permissions=[permission_smart_link_edit], text=_('edit'), view='linking:smart_link_edit', args='object.pk')
link_smart_link_instance_view = Link(permissions=[permission_smart_link_view], text=_('documents'), view='linking:smart_link_instance_view', args=['document.pk', 'object.smart_link.pk'])
link_smart_link_instances_for_document = Link(permissions=[permission_document_view], text=_('smart links'), view='linking:smart_link_instances_for_document', args='object.pk')
link_smart_link_list = Link(permissions=[permission_smart_link_create], text=_('smart links'), view='linking:smart_link_list')
link_smart_link_setup = Link(icon='fa fa-link', permissions=[permission_smart_link_create], text=_('smart links'), view='linking:smart_link_list')
