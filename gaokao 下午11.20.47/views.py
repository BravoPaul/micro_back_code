from django.shortcuts import get_object_or_404, render
from .models import School, SchoolList, SchoolDetail, SchoolScore
from django.http import HttpResponse
from django.core import serializers
from itertools import chain
from django.db.models import Count
from .recommend import Recommend
import json


# Create your views here.

# Create your views here.
def listmeta(request):
    result = []
    index_data = SchoolList.objects.values('condition').annotate(total=Count('school_id'))
    for one_data in index_data:
        result.append(one_data)
    response = json.dumps(result)
    return HttpResponse(response, content_type="application/json")


def list(request):
    school_list = []
    page_num_ex = int(request.POST.get('page_num_ex'))
    page_num_post = int(request.POST.get('page_num_post'))
    if request.POST.get('condition') == '全部院校':
        result_list = School.objects.all()[page_num_ex * 30:page_num_post * 30]
    else:
        index = request.POST.get('condition')
        schoolindexlist = SchoolList.objects.filter(condition=index)
        for sch in schoolindexlist:
            school_list += School.objects.filter(sch_id=sch.school_id)
        result_list = school_list[page_num_ex * 30:page_num_post * 30]
    result_final = serializers.serialize('json', result_list)
    return HttpResponse(result_final, content_type="application/json")


def detail(request):
    sch_id = request.POST.get('sch_id')
    school_intro = School.objects.get(sch_id=sch_id)
    school_detail = school_intro.schooldetail_set.all()
    school_rank = school_intro.schoolrank_set.all()
    school_famous = school_intro.schoolfamous_set.all()
    school_score = school_intro.schoolscore_set.all()
    school_major = school_intro.schoolmajor_set.all()
    school_intro = [school_intro]
    result_list = chain(school_intro, school_detail, school_rank, school_famous, school_score, school_major)
    result_final = serializers.serialize('json', result_list)
    return HttpResponse(result_final, content_type="application/json", charset='utf-8')


def recommend(request):
    '''
    :param request:
    :return: #
    {
        #     sch_id:dd,
        #     name:name,
        #     tags:ff
        #     location:ff
        #     logo:ff
        #     min_score:cc
        #     enroll_num:cc
        #     probability:cc
        #     major:{
        #         name:
        #         probability:
        #         tuition:
        #         min_score:
        #         enroll_num:
        #     },
        #
    }
    '''

    province_id = request.POST.get('province_id')
    wenli = request.POST.get('wenli')
    score = request.POST.get('score')
    academic_year = request.POST.get('academic_year')
    rec = Recommend()
    result = rec.get_recommend_result(province_id, wenli, score,academic_year)
    for key, values in result.items():
        for one_value in values:
            school_intro = School.objects.get(sch_id=one_value['sch_id'])
            sch_score = school_intro.schoolscore_set.filter(
                academic_year=academic_year,
                wenli=wenli,
                batch_name=key
            )
            if len(sch_score)==0:
                one_value['min_score'] = '-'
                one_value['admission_count'] = '-'
            else:
                if int(sch_score[0].min_score)>0 and int(sch_score[0].min_score)<1000:
                    score_format = sch_score[0].min_score
                else:
                    score_format = '-'
                if int(sch_score[0].admission_count)>0 and int(sch_score[0].admission_count)<100000:
                    admission_format = sch_score[0].admission_count
                else:
                    admission_format = '-'
                one_value['min_score'] = score_format
                one_value['admission_count'] = admission_format
            one_value['sch_logo'] = str(school_intro.sch_logo)
            one_value['location'] = school_intro.location
            one_value['sch_tags'] = school_intro.sch_tags
            one_value['sch_name'] = school_intro.sch_name

            school_major = school_intro.schoolmajor_set.filter(
                academic_year=academic_year,
                wenli=wenli,
                batch_name=key
            )
            for one_major in school_major:
                major = {}
                major['probability'] = one_value['probability']
                if int(one_major.min_score)>0 and int(one_major.min_score)<1000:
                    score_format = sch_score[0].min_score
                else:
                    score_format = '-'
                if int(one_major.admission_count)>0 and int(one_major.admission_count)<100000:
                    admission_format = sch_score[0].admission_count
                else:
                    admission_format = '-'
                major['min_score'] = score_format
                major['enroll_major_name'] = one_major.enroll_major_name
                major['admission_count'] = admission_format
                major['tuition'] = one_major.tuition
                major['academic_rule'] = one_major.academic_rule

                try:
                    one_value['major'].append(major)
                except KeyError:
                    one_value['major'] = [major]



    response = json.dumps(result)
    return HttpResponse(response, content_type="application/json")



# def score(request):
#     sch_id = request.POST.get('sch_id')
#     school_intro = School.objects.get(sch_id=sch_id)
#     school_score = school_intro.schoolscore_set.all()
#     result_final = serializers.serialize('json', school_score)
#     return HttpResponse(result_final, content_type="application/json", charset='utf-8')
