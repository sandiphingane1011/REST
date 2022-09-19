from wsgiref.validate import validator
from rest_framework import serializers 
from first_app.models import Student


# class based
"""
def name_startswith_R(value):
    if value[0].lower() == 'r':
        return value
    raise serializers.ValidationError("Name should start with R or r")

def name_len(value):
    if len(value) >= 4:
        return value
    raise serializers.ValidationError("Len of name should be always greter then 4")





class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[name_startswith_R, name_len])
    age =  serializers.IntegerField()
    city =  serializers.CharField(max_length=100)
    marks = serializers.IntegerField()

    def create(self, validated_data):
        stud = Student.objects.create(**validated_data)
        return stud

    def update(self,instance, validated_data):  # python dict
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city) # NOne
        instance.marks = validated_data.get('marks', instance.marks)  # None
        instance.save()
        return instance


    #field level validation

    # def validation_age(self,value):
    #     print("validate age")
    #     if value >= 21:
    #         return value
    #     raise serializers.ValidationError("Age less then 21 is not allowed..")


    # def validate_marks(self, value):
    #     print("validate marks")
    #     return value 

    #object level validation 
    # def validate(self, data):
    #     print("in validate method")
    #     if (data.get("city") == "pune") and (data.get("age") >= 21):
    #         return data
    #     raise serializers.ValidationError("City must be pune and age must be above 21")"""



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name', 'age', 'city','marks']
        fields = '__all__'
        # exclude = ['id','marks']
        # read_only_fields = ['name']
        # extra_kwargs = {"name": {'read_only': True},"age": {"write_only": True},"city": {'read_only': True}}


    #field level validation 
    def validate_age(self, value):
        print("validate age")
        if value >= 21:
            return value
        raise serializers.ValidationError("age less then 21 is not allowed..")