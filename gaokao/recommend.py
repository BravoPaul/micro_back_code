# python manage.py shell < /Users/kunyue/project_personal/my_project/mysite/gaokao/recommend.py
from gaokao.models import SchoolScore, School, GaokaoRecallScore, GaokaoRecallRank, GaokaoMetaScoreLine, SchoolMajor,MajorSplit


class Recommend(object):

    # 专业改名字了怎么办
    # 新专业怎么办
    def get_recommend_result(self, province_id, wenli, score, year):
        '''
        推荐接口关注的是用户对于所有学校所有专业的概率，而学校的录取概率为所有专业录取概率最低值
        :param province_id: 省份
        :param wenli: 1：文科；2：理科
        :param score: 高考分
        :return:
        '''
        recallResult = self.recallScore(province_id, wenli, score, year)
        rankResult = self.rank(province_id, wenli, score, year, recallResult)
        return rankResult

    def rank(self, province_id, wenli, score, year, recallResult):
        result_school_major = []
        # 差多少分，录取概率是多少
        for one_data in recallResult:
            school_intro = School.objects.get(sch_id=one_data.sch_id)
            school_majors = school_intro.schoolmajor_set.filter(academic_year=year)
            for one_sch_major in school_majors:
                major_split = MajorSplit.objects.filter(major_name=one_sch_major.enroll_major_name)


            result_school_major.append()

        return recallResult

    def recallScore(self, province_id, wenli, score, year):
        '''
        召回分为3种，肯定能上的，肯定不能上的和不确定的，打分的意义在于给不确定的打分
        :param province_id:
        :param wenli:
        :param score:
        :return:
        '''

        result = {
            '本科第一批': [],
            '本科第二批': [],
            '高职专科批': [],
        }
        score_line = GaokaoMetaScoreLine.objects.filter(
            province_id=province_id,
            wenli=wenli,
            academic_year=year
        )
        print(score_line)
        for one_line in score_line:
            score_diff = int(score) - int(one_line.school_line)
            print('正在预测', one_line.batch_name, score_diff)
            recall_data = GaokaoRecallScore.objects.filter(
                province_id=province_id,
                wenli=wenli,
                batch_name=one_line.batch_name,
            )
            scores = []
            for one_data in recall_data:
                scores.append(one_data.score)
                if one_data.score == score_diff:
                    sch_wins = one_data.school_win.split(',')[0:5]
                    school_loses = one_data.school_lose.split(',')[0:5]
                    school_predicts = one_data.school_predict.split(',')
                    for one_sch in sch_wins:
                        result[one_line.batch_name].append({'sch_id': one_sch, 'probability': 90})
                    for one_sch in school_loses:
                        result[one_line.batch_name].append({'sch_id': one_sch, 'probability': 10})
                    for one_sch in school_predicts:
                        result[one_line.batch_name].append({'sch_id': one_sch, 'probability': 50})

            print(len(result[one_line.batch_name]))

            if len(result[one_line.batch_name]) == 0:
                max_score = max(scores)
                min_score = max(scores)
                max_index = scores.index(max_score)
                min_index = scores.index(min_score)
                if score_diff > max_score:
                    print('这里max')
                    sch_wins = recall_data[max_index].school_win.split(',')[0:30]
                    school_predicts = recall_data[max_index].school_predict.split(',')

                    for one_sch in sch_wins:
                        if one_sch != '':
                            result[one_line.batch_name].append({'sch_id': one_sch, 'probability': 90})
                    for one_sch in school_predicts:
                        if one_sch != '':
                            result[one_line.batch_name].append({'sch_id': one_sch, 'probability': 90})
                elif score_diff < min_score:
                    print('这里min')
                    school_loses = recall_data[min_index].school_lose.split(',')[0:30]
                    school_predicts = recall_data[min_index].school_predict.split(',')
                    for one_sch in school_loses:
                        if one_sch != '':
                            result[one_line.batch_name].append({'sch_id': one_sch, 'probability': 10})
                    for one_sch in school_predicts:
                        if one_sch != '':
                            result[one_line.batch_name].append({'sch_id': one_sch, 'probability': 10})
                else:
                    raise ValueError

        # print(result)

        return result

    def recallRank(self, province_id, wenli, score):
        '''
        召回分为3种，肯定能上的，肯定不能上的和不确定的，打分的意义在于给不确定的打分
        :param province_id:
        :param wenli:
        :param score:
        :return:
        '''
        pass
