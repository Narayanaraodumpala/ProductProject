from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from app1.serializers import ProductSerializer,UserSerializer,OrderSerializer
from app1.models import Product,User,Order

class InsertProduct(APIView):
    def post(self,request):
        ps = ProductSerializer(data=request.data)
        if ps.is_valid():
            ps.save()
            message = {"message":"Product Saved"}
        else:
            message = {"error":ps.errors}
        return Response(message)

    def get(self,request):
        qs = Product.objects.all()
        ps = ProductSerializer(qs,many=True)
        return Response(ps.data)

class Read1Product(APIView):
    def get(self,request,product_id):
        try:
            res = Product.objects.get(no=product_id)
            return Response(ProductSerializer(res).data)
        except Product.DoesNotExist:
            message = {"error": "Product id is Invalid"}
            return Response(message)

    def put(self,request,product_id):
        try:
            res = Product.objects.get(no=product_id)
            d1 = request.data
            ps = ProductSerializer(res,d1,partial=True)
            if ps.is_valid():
                ps.save()
                message = {"message": "Product Updated"}
            else:
                message = {"error": ps.errors}
            return Response(message)
        except Product.DoesNotExist:
            message = {"error":"Product id is Invalid"}
            return Response(message)

    def delete(self,request,product_id):
            res = Product.objects.filter(no=product_id).delete()
            if res[0] != 0:
                message = {"message": "Product is Deleted"}
            else:
                message = {"message": "Invalid Product"}
            return Response(message)

class User(APIView):
    def post(self, request):
        ps = UserSerializer(data=request.data)
        if ps.is_valid():
            ps.save()
            message = {"message": "user Saved"}
        else:
            message = {"error": ps.errors}
        return Response(message)

    def get(self, request):
        qs = User.objects.all()
        ps = UserSerializer(qs, many=True)
        return Response(ps.data)


class Read1User(APIView):
    def get(self, request, user_id):
        try:
            res = User.objects.get(no=user_id)
            return Response(UserSerializer(res).data)
        except User.DoesNotExist:
            message = {"error": "User id is Invalid"}
            return Response(message)

    def put(self, request,user_id):
        try:
            res = User.objects.get(no=user_id)
            d1 = request.data
            ps = UserSerializer(res, d1, partial=True)
            if ps.is_valid():
                ps.save()
                message = {"message": "user Updated"}
            else:
                message = {"error": ps.errors}
            return Response(message)
        except User.DoesNotExist:
            message = {"error": "user id is Invalid"}
            return Response(message)

    def delete(self, request, user_id):
        res = User.objects.filter(no=user_id).delete()
        if res[0] != 0:
            message = {"message": "user is Deleted"}
        else:
            message = {"message": "Invalid user"}
        return Response(message)


class Order(APIView):
    def post(self,request):
        ps = OrderSerializer(data=request.data)
        if ps.is_valid():
            ps.save()
            message = {"message":"order Saved"}
        else:
            message = {"error":ps.errors}
        return Response(message)

    def get(self,request):
        qs = Order.objects.all()
        ps = OrderSerializer(qs,many=True)
        return Response(ps.data)


class Read1Order(APIView):
    def get(self, request, order_id):
        try:
            res = Order.objects.get(no=order_id)
            return Response(OrderSerializer(res).data)
        except Order.DoesNotExist:
            message = {"error": "order id is Invalid"}
            return Response(message)

    def put(self, request, order_id):
        try:
            res = Order.objects.get(no=order_id)
            d1 = request.data
            ps = OrderSerializer(res, d1, partial=True)
            if ps.is_valid():
                ps.save()
                message = {"message": "order Updated"}
            else:
                message = {"error": ps.errors}
            return Response(message)
        except Order.DoesNotExist:
            message = {"error": "Order id is Invalid"}
            return Response(message)

    def delete(self, request, order_id):
        res = Order.objects.filter(no=order_id).delete()
        if res[0] != 0:
            message = {"message": "order is Deleted"}
        else:
            message = {"message": "Invalid order"}
        return Response(message)
