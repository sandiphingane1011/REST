from email.mime import application
import json
from mimetypes import common_types
from urllib import request
from django import views
from django.shortcuts import render
from first_app.models import Student
from first_app.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView



# from rest_framework.decorators import cs

# Create your views here.


def single_stud(request, pk):
    print("in single stud API")
    stud_obj =  Student.objects.get(id=pk)   # complex data type
    python_obj = StudentSerializer(stud_obj)  # complex data type to native python type
    json_data = JSONRenderer().render(python_obj.data)  # python to json
    return HttpResponse(json_data, content_type='application/json')

def all_stud(request):
    print("In all stud API", '####')
    studs = Student.objects.all()
    python_obj = StudentSerializer(studs, many=True)  
    json_data = JSONRenderer().render(python_obj.data) 
    return HttpResponse(json_data, content_type='application/json')


import io
@csrf_exempt
def create_data(request):
    if request.method == 'POST':
       # print(request.boby)
        bytes_data = request.body
        streamed_data = io.BytesIO(bytes_data)
        python_data = JSONParser().parse(streamed_data)
        # print(python_data)      # {'name': 'ccc', 'age': 19, 'city': 'Nanded', 'marks': 70}
        ser = StudentSerializer(data=python_data)
        print(ser)
        if ser.is_valid():
            ser.save()   # calls create() method of StudentSerialiazer
            msg = {"msg": "data created successfully...!"}
            res = JSONRenderer().render(msg)
        return HttpResponse(res, content_type='application/json')
    else:
        msg = {"error": "only post method allowed"}
        res = JSONRenderer().render(msg)
        return HttpResponse("Only post request accepted..!")

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def common_line(request):
    bytes_data = request.body
    streamed_data = io.BytesIO(bytes_data) # json data
    python_dict = JSONParser().parse(streamed_data) 
    return python_dict
"""

@csrf_exempt
@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == 'GET':  # id pass ---- single data, id {} - all data,
        bytes_data = request.body
        streamed_data = io.BytesIO(bytes_data) # json data
        python_dict = JSONParser().parse(streamed_data)  # dict -- {} or {"id": 1}
        sid = python_dict.get("id")  # None 

        if sid:
            # for single data
            try:
                stud = Student.objects.get(id=sid)
            except Student.DoesNotExist:
                msg = {"error": "given id does not exits...!"}
                res = JSONRenderer().render(msg)
                return HttpResponse(res, content_type='application/json')


            ser = StudentSerializer(stud)   # complex to native python
            # json_data = JSONRenderer().render(ser.data)
            # return HttpResponse(json_data, content_type='application/json')



        # single line
        return JsonResponse(ser.data)



        # for all data
        studs = Student.objects.all()
        ser = StudentSerializer(studs, many=True)
        # json_data = JSONRenderer().render(ser.data) 
        # return HttpResponse(json_data, content_type='application/json')


        return JsonResponse(ser.data, safe=False)









    elif request.method == 'POST':   # user data send
        # data1 = request.data
        byte_data = request.body
        streamed_data = io.BytesIO(byte_data)
        json_py = JSONParser().parse(streamed_data)
        print(json_py)
        ser = StudentSerializer(data =json_py)
        if ser.is_valid():
            
            ser.save()
            return JsonResponse({"msg": "data inserted succesfully..!"})
        return JsonResponse({"msg":ser.errors}) 





        # ser = StudentSerializer(data=python_dict)
        # if ser.is_valid():
        #     ser.save()
        #     return JsonResponse({"msg": "data inserted succesfully..!"})
        # return JsonResponse({"error": "ser.errors"})

       
    elif request.method == 'PUT':   # id -along with data which is to be updated
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data) # json data
        # python_dict = JSONParser().parse(streamed_data)  # dict -- {} or {"id": 1}


        sid = python_dict.get("id")  # None
        print(python_dict)
        if sid:
        #print(python_dict)
            stud = Student.objects.get(id=sid)

        ser = StudentSerializer(instance=stud, data=python_dict,)
        if ser.is_valid():
            ser.save

        ser = StudentSerializer(data=python_dict)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg": "data inserted succesfully..!"})
        return JsonResponse({"error": "invalid"}) 
        # print(python_dict)
        ser = StudentSerializer(instance=stud, data=python_dict, partial=True)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg": "data inserted succesfully..!"})
        return JsonResponse({"error":  ser.errors})

    elif request.method == 'DELETE':   # user id
        # bytes_data = request.body
        # streamed_data = io.BytesIO(bytes_data) # json data
        # python_dict = JSONParser().parse(streamed_data)  # dict -- {} or {"id": 1}
        

        sid = python_dict.get("id")  # None
        print(python_dict)
        if sid:
            stud = Student.objects.get(id=sid)
            stud.delete()
            return JsonResponse({"msg":  "data deleted succesfully...!"})
    else:
        msg = {"error": "invalid request method"} # python dict
        res = JSONRenderer().render(msg)  # json madhe convert
        return HttpResponse(res, content_type='application/json')

  """

  #class based view
from django.views import View
from django.utils.decorators import method_decorator

 
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        python_dict = JSONParser().parse(stream= '')  # dict -- {} or {"id": 1}
        sid = python_dict.get("id")  # None 

        if sid:
            # for single data
            try:
                stud = Student.objects.get(id=sid)
            except Student.DoesNotExist:
                msg = {"error": "given id does not exits...!"}
                res = JSONRenderer().render(msg)
                return HttpResponse(res, content_type='application/json')


            ser = StudentSerializer(stud)   # complex to native python
            # json_data = JSONRenderer().render(ser.data)
            # return HttpResponse(json_data, content_type='application/json')



        # single line
        return JsonResponse(ser.data)



        # for all data
        studs = Student.objects.all()
        ser = StudentSerializer(studs, many=True)
        # json_data = JSONRenderer().render(ser.data) 
        # return HttpResponse(json_data, content_type='application/json')


        return JsonResponse(ser.data, safe=False)



    def post(self, request, *args, **kwargs):

        python_dict = common_line(request)
        ser = StudentSerializer(data=python_dict)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg": "data inserted succesfully..!"})
        return JsonResponse({"error": "ser.errors"})


    def put(self, request, *args, **kwargs):
        python_dict = common_line(request)  # dict -- {} or {"id": 1}


        sid = python_dict.get("id")  # None
        print(python_dict)
        if sid:
        #print(python_dict)
            stud = Student.objects.get(id=sid)

        ser = StudentSerializer(instance=stud, data=python_dict,)
        if ser.is_valid():
            ser.save

        ser = StudentSerializer(data=python_dict)
        if ser.is_valid():
            ser.save()
            return JsonResponse({"msg": "data inserted succesfully..!"})
        return JsonResponse({"error": "invalid"}) 
        # print(python_dict)

    def delete(self, request, *args, **kwargs):
        python_dict = JSONParser().parse(stremed)  # dict -- {} or {"id": 1}
        

        sid = python_dict.get("id")  # None
        print(python_dict)
        if sid:
            stud = Student.objects.get(id=sid)
            stud.delete()
            return JsonResponse({"msg":  "data deleted succesfully...!"})    


# api_view --
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','post', 'put', 'delete','PATCH'])
def student_api(request,pk=None):
    if request.method == 'GET':
        sid = request.data.get('id')
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data)
        else:
            studs = Student.objects.all()
            ser = StudentSerializer(studs,many=True)
            return Response(ser.data)

        
    elif request.method == 'POST':
        print(request.data)    # parse - python dict
        data1 = request.data
        ser = StudentSerializer(data=data1)
        if ser.is_valid():
            ser.save()
            return Response({"msg": "Data Created", "data": request.data},status=status.HTTP_201_CREATED)
        else:
            return Response(ser.error)

    elif request.method == 'PUT':
        stud = Student.objects.get(id=pk)       # request.data.get('id'))
        ser = StudentSerializer(instance=stud, data=request.data,)
        if ser.is_valid():
            ser.save()
            return Response({'msg': "complete Data update for {}".format(pk)}) 

    elif request.method == 'PATCH':
        stud = Student.objects.get(id=pk)
        ser = StudentSerializer(instance=stud, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg': "Partial Data update for {}".format(pk)})        


    elif request.method == 'DELETE':
        pass


##########################################################

#- @api_view 
# APIView class -sub class of view----




class StudentAPINew(APIView):
    def get(self, request, pk=None, format=None):
        sid = pk 
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(stud)
            return Response(ser.data)

        studs = Student.objects.all()
        ser = StudentSerializer(studs, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        data = request.data   # python dict
        ser = StudentSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({"msg": "data created..", "data": request.data}, status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, pk,request, format=None):
        sid = pk 
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instantce=stud, data=request.data)
            if ser.is_valid():
                ser.save()
            return Response({"msg": "data created..", "data": request.data}, status=status.HTTP_200_ok)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
   
    def patch(self, pk,request, format=None):
        sid = pk 
        if sid:
            stud = Student.objects.get(id=sid)
            ser = StudentSerializer(instantce=stud, data=request.data)
            if ser.is_valid():
                ser.save()
            return Response({"msg": "data created..", "data": request.data}, status=status.HTTP_200_ok)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)



    def delete(self,  pk,request,  format=None):
        pass 

# GenericAPIView and Mixins 
# already defined common behaviours--

#-- queryset --Student.objects.all()
# --serializer_class -- StudentSerializer

# Mixinz:- 
# ListModelMixin -- all data
# RetriveModelMixin -- single data
# CreateModelMixin  -- for post request
# UpdateModeMixin -- update
# DestroyModelMixin -- delete


from rest_framework.mixins import ListModelMixin,RetrieveModelMixin, CreateModelMixin,UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView

class StudList(GenericAPIView, ListModelMixin):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer

   def get(self, request, *args,  **kwargs):
       return self.list(self, request, *args, **kwargs)  # ListModeMixin
    





class StudCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args,  **kwargs):
       return self.create(request, *args, **kwargs) 

class StudRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args,  **kwargs):
       return self.retrieve(self, request, *args, **kwargs) 

   
class StudUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args,  **kwargs):
       return self.update(self, request, *args, **kwargs)


class StudDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args,  **kwargs):
       return self.destroy(request, *args, **kwargs)

# combined mixins

class StudListCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args,  **kwargs):
       return self.list(self, request, *args, **kwargs)

    def post(self, request, *args,  **kwargs):
       return self.create(self, request, *args, **kwargs)

class StudRetrieveUpdateDestroy(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args,  **kwargs):
       return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args,  **kwargs):
       return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args,  **kwargs):
       return self.destroy(request, *args, **kwargs)
