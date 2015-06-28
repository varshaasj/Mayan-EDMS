from __future__ import absolute_import, unicode_literals

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from rest_framework import generics

from acls.models import AccessEntry
from documents.models import Document
from documents.permissions import permission_document_view
from permissions.models import Permission
from rest_api.filters import MayanObjectPermissionsFilter
from rest_api.permissions import MayanPermission

from .models import Index, IndexInstanceNode, IndexTemplateNode
from .permissions import (permission_document_indexing_create,
                          permission_document_indexing_delete,
                          permission_document_indexing_edit,
                          permission_document_indexing_view)
from .serializers import (IndexInstanceNodeSerializer, IndexSerializer,
                          IndexTemplateNodeSerializer)


class APIIndexListView(generics.ListCreateAPIView):
    serializer_class = IndexSerializer
    queryset = Index.objects.all()

    filter_backends = (MayanObjectPermissionsFilter,)
    mayan_object_permissions = {'GET': [permission_document_indexing_view]}
    mayan_view_permissions = {'POST': [permission_document_indexing_create]}

    def get(self, *args, **kwargs):
        """Returns a list of all the defined indexes."""
        return super(APIIndexListView, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Create a new index."""
        return super(APIIndexListView, self).post(*args, **kwargs)


class APIIndexView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IndexSerializer
    queryset = Index.objects.all()

    permission_classes = (MayanPermission,)
    mayan_object_permissions = {
        'GET': [permission_document_indexing_view],
        'PUT': [permission_document_indexing_edit],
        'PATCH': [permission_document_indexing_edit],
        'DELETE': [permission_document_indexing_delete]
    }

    def delete(self, *args, **kwargs):
        """Delete the selected index."""
        return super(APIIndexView, self).delete(*args, **kwargs)

    def get(self, *args, **kwargs):
        """Returns the details of the selected index."""
        return super(APIIndexView, self).get(*args, **kwargs)

    def patch(self, *args, **kwargs):
        """Partially edit an index."""
        return super(APIIndexView, self).patch(*args, **kwargs)

    def put(self, *args, **kwargs):
        """Edit an index."""
        return super(APIIndexView, self).put(*args, **kwargs)


class APIIndexNodeInstanceDocumentListView(generics.ListAPIView):
    """
    Returns a list of all the documents contained by a particular index node instance.
    """

    filter_backends = (MayanObjectPermissionsFilter,)
    mayan_object_permissions = {'GET': [permission_document_view]}

    def get_serializer_class(self):
        from documents.serializers import DocumentSerializer
        return DocumentSerializer

    def get_queryset(self):
        index_node_instance = get_object_or_404(IndexInstanceNode, pk=self.kwargs['pk'])
        try:
            Permission.objects.check_permissions(self.request.user, [permission_document_indexing_view])
        except PermissionDenied:
            AccessEntry.objects.check_access(permission_document_indexing_view, self.request.user, index_node_instance.index)

        return index_node_instance.documents.all()


class APIIndexTemplateListView(generics.ListAPIView):
    serializer_class = IndexTemplateNodeSerializer

    filter_backends = (MayanObjectPermissionsFilter,)
    mayan_object_permissions = {'GET': [permission_document_indexing_view]}

    def get(self, *args, **kwargs):
        """Returns a list of all the template nodes for the selected index."""
        return super(APIIndexTemplateListView, self).get(*args, **kwargs)


class APIIndexTemplateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IndexTemplateNodeSerializer
    queryset = IndexTemplateNode.objects.all()

    permission_classes = (MayanPermission,)
    mayan_object_permissions = {
        'GET': [permission_document_indexing_view],
        'PUT': [permission_document_indexing_edit],
        'PATCH': [permission_document_indexing_edit],
        'DELETE': [permission_document_indexing_edit]
    }

    def delete(self, *args, **kwargs):
        """Delete the selected index template node."""
        return super(APIIndexTemplateView, self).delete(*args, **kwargs)

    def get(self, *args, **kwargs):
        """Returns the details of the selected index template node."""
        return super(APIIndexTemplateView, self).get(*args, **kwargs)

    def patch(self, *args, **kwargs):
        """Partially edit an index template node."""
        return super(APIIndexTemplateView, self).patch(*args, **kwargs)

    def put(self, *args, **kwargs):
        """Edit an index template node."""
        return super(APIIndexTemplateView, self).put(*args, **kwargs)


class APIDocumentIndexListView(generics.ListAPIView):
    """
    Returns a list of all the indexes to which a document belongs.
    """

    serializer_class = IndexInstanceNodeSerializer

    filter_backends = (MayanObjectPermissionsFilter,)
    mayan_object_permissions = {'GET': [permission_document_indexing_view]}

    def get_queryset(self):
        document = get_object_or_404(Document, pk=self.kwargs['pk'])
        try:
            Permission.objects.check_permissions(self.request.user, [permission_document_view])
        except PermissionDenied:
            AccessEntry.objects.check_access(permission_document_view, self.request.user, document)

        return document.node_instances.all()
