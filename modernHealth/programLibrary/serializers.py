from rest_framework import serializers
from modernHealth.programLibrary.models import HTML, Section, Program, MCQ

class HTMLSerializer(serializers.ModelSerializer):

    class Meta:
        model = HTML
        fields = ['encodedContent']


class MCQSerializer(serializers.ModelSerializer):

    class Meta:
        model = MCQ
        fields = ['question', 'optionOne', 'optionTwo', 'optionThree', 'optionFour', 'optionFive']


class SectionSerializer(serializers.ModelSerializer):
    html = HTMLSerializer(read_only=True, many=True)
    mcq = MCQSerializer(read_only=True, many=True)

    class Meta:
        fields = ['name', 'description', 'overviewImage', 'orderIndex', 'activityType', 'mcq', 'html']
        model = Section


class ProgramSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(read_only=True, many=True)

    class Meta:
        fields = ['name', 'description', 'sections']
        model = Program
