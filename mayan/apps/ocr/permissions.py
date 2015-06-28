from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from permissions.models import PermissionNamespace

namespace = PermissionNamespace('ocr', _('OCR'))

permission_ocr_document = namespace.add_permission(name='ocr_document', label=_('Submit documents for OCR'))
permission_ocr_document_delete = namespace.add_permission(name='ocr_document_delete', label=_('Delete documents from OCR queue'))
permission_ocr_content_view = namespace.add_permission(name='ocr_content_view', label=_('Can view the transcribed text from document'))
permission_document_type_ocr_setup = namespace.add_permission(name='ocr_document_type_setup', label=_('Change document type OCR settings'))
