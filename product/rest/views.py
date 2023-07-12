from product.rest.serializers import ProductCategorySerializer, ProductBrandSerializer, \
    ProductSerializer, ProductDetailSerializer, ProductImageSerializer, ProductTagSerializer
from rest_framework.decorators import action
from product.models import ProductCategory, ProductBrand, Product, ProductTag
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics, serializers, filters, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny
from product.rest.permissions import AdminOrReadOnly
from rest_framework import viewsets
from product.rest.pagination import ProductPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

# filter category by admin
class ProductCategoryViewBYAdmin(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'is_active', 'is_delete']
    search_fields = ['^title']


# filter category by user is not authenticated
class ProductCategoryView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    def get_queryset(self):
        title = self.kwargs['title']
        return ProductCategory.objects.filter(title__exact=title)


# get by id and update and delete category by admin
class ProductCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = ProductCategorySerializer
    model = ProductCategory
    def get_queryset(self):
        pk = self.kwargs['pk']
        return ProductCategory.objects.filter(id=pk)

# save category by admin
class ProductCategoryCreateView(APIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAdminUser]
    def post(self, request):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# filter brand by admin
class ProductBrandViewBYAdmin(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductBrandSerializer
    queryset = ProductBrand.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'is_active']
    search_fields = ['^title']

# filter title by user is not authenticated
class ProductBrandView(generics.ListAPIView):
    serializer_class = ProductBrandSerializer
    queryset = ProductBrand.objects.all()

    def get_queryset(self):
        title = self.kwargs['title']
        return ProductBrand.objects.filter(title__exact=title)

# get by id and update and delete category by admin
class ProductBrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductBrandSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return ProductBrand.objects.filter(id=pk)

# save brand by admin
class ProductBrandCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = ProductBrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# show products all of one brand
class BrandOfProduct(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AdminOrReadOnly]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Product.objects.filter(brand=pk)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination

    def _params_to_ints(self, qs):
        return [int(str_id) for str_id in qs.split(',')]
    def get_queryset(self):
        category = self.request.query_params.get('category')
        queryset = self.queryset
        if category:
            category_ids = self._params_to_ints(category)
            return queryset.filter(category__id__in=category_ids)

        else:
            return self.queryset.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer

        elif self.action == 'upload_image':
            return ProductImageSerializer
        return self.serializer_class
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save()

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer(
            product,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,

            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductTagViewSet(viewsets.ModelViewSet):
    serializer_class = ProductTagSerializer
    queryset = ProductTag.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AdminOrReadOnly]
        return [permission() for permission in permission_classes]


class TagsOfProduct(generics.ListAPIView):
    serializer_class = ProductTagSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return ProductTag.objects.filter(product=pk)







