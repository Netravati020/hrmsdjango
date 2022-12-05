
from MySQLdb._exceptions import IntegrityError
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Employees

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields='__all__'




class BulkCreateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result= list()
        for attrs in validated_data:
            result.append(self.child.create(attrs))
        try:
            print('bulk insert------------------', self.child.Meta.model)
            self.child.Meta.model.objects.bulk_create(result,batch_size=2000)
        except IntegrityError as e:
            raise ValidationError(e)
        return result
    def update(self, instances, validated_data):
        instance_hash= {index: instance for index, instance in enumerate(instances)}
        result= [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]
        writable_fields= [
            field.name for field in self.child.Meta.model.meta.get_fields()
            if field.name not in self.child.Meta.read_only_fields

        ]
        try:
            self.child.Meta.model.objects.bulk_update(result,writable_fields, batch_size=2000)
        except IntegrityError as e:
            raise ValidationError(e)
        return result


class Employeeupdateserializer(serializers.ModelSerializer):
    def create(self,validated_data):
        if isinstance(self._kwargs['data'], dict):
            return super().create( validated_data)
        print('validated', validated_data)
        instance= Employees(**validated_data)
        return instance

    def update(self, instance, validated_data):
        if isinstance(self._kwargs["data"], dict):
            return super().update(instance, validated_data)

        for k, v in validated_data.items():
                setattr(instance, k,v)
        return instance

    class Meta:
        model= Employees
        fields= '__all__'
        list_serializer_class=BulkCreateSerializer


