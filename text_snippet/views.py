from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from text_snippet.models import TextSnippet, Tag
from text_saver_admaren.responses import serializer_error_response
from text_snippet.serializers import TextSnippetOverviewSerializers, TextSnippetSerializer, TagSerializer


class TextSnippetViewSet(viewsets.ModelViewSet):
    # optimized query by using select_related
    queryset = TextSnippet.objects.select_related('tag').select_related('created_by').filter(is_deleted=False)
    permission_classes = (IsAuthenticated,)
    serializer_class = TextSnippetSerializer

    def list(self, request, *args, **kwargs):
        '''
        list will return the total count of text snippets and the active snippets with a hyperlink to respective detail APIs.
        '''
        texts = self.get_queryset()
        serializer = TextSnippetOverviewSerializers(texts, context={'request': request}, many=True)
        # total count of text snippets in the DB
        total_count = texts.count()
        return Response({
            'success': True,
            'message': 'Successfully fetched text_snippet snippets overview.',
            'total_count': total_count,
            'data': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        '''
        API for creating new snippet
        '''
        serializer = self.get_serializer(data=request.data, context={'user': request.user})
        # checking for data validation
        if serializer.is_valid():
            # creating new text snippet
            serializer.save()
            return Response({
                'success': True,
                'message': 'Successfully created text_snippet snippet.',
                'data': serializer.data
            },
                status=status.HTTP_201_CREATED
            )
        return serializer_error_response(serializer.errors)

    def retrieve(self, request, *args, **kwargs):
        '''
        Retrieves the text snippet details
        '''

        # getting the instance using primary key(pk)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'success': True,
            'message': 'Successfully fetched text_snippet snippet details.',
            'data': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def partial_update(self, request, *args, **kwargs):
        '''
        Updates the text snippet
        '''

        # getting the instance using primary key(pk)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        # checking field validation
        if serializer.is_valid():
            # updating the text snippet
            serializer.save()
            return Response({
                'success': True,
                'message': 'Successfully updated text_snippet snippet.',
                'data': self.get_serializer(instance).data
            },
                status=status.HTTP_200_OK
            )
        return serializer_error_response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        '''
        Deletes the text snippet by setting the is_deleted parameter as 'FALSE'
        '''
        # getting the instance using primary key(pk)
        instance = self.get_object()
        # setting the is_deleted parameter as True
        instance.is_deleted = True
        instance.save()
        # returning the list of remaining snippets
        return self.list(request)


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    # reduced query expense by pre-fetching the related text_snippets
    queryset = Tag.objects.prefetch_related('texts').all()
    serializer_class = TagSerializer

    def list(self, request, *args, **kwargs):
        '''
            Returns the list of tags with their id and title
        '''

        # get all tag id and title
        tags = self.get_queryset().values('id', 'title')
        return Response({
            'success': True,
            'message': 'Successfully updated tags.',
            'data': tags
        },
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        '''
        Returns the details of text snippets under a particular tag.
        '''

        # getting the object using primary key(pk)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'success': True,
            'message': 'Successfully updated tag details',
            'data': serializer.data
        },
            status=status.HTTP_200_OK
        )
