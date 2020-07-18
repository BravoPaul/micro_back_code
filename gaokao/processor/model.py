import pandas as pd


#
# 用户特征
# score_user
# rank_user
# wenli
# province_id

# 学校特征
# sch_id
# batch_id
# major_id
# sch_score_min
# sch_score_max
# sch_score_avg
# score_min_mean
# score_min_std
# score_min_trend
# score_avg_mean
# score_avg_std
# score_avg_trend
# score_max_mean
# score_max_std
# score_max_trend
# sch_enroll_plan
# major_enroll_plan
# rank_min_mean
# rank_min_std
# rank_min_trend
# rank_avg_mean
# rank_avg_std
# rank_avg_trend
# rank_max_mean
# rank_max_std
# rank_max_trend

# sch_major_1_id
# sch_major_1_min_mean
# sch_major_1_min_std
# sch_major_1_min_trend
# sch_major_2_id
# sch_major_2_min_mean
# sch_major_2_min_std
# sch_major_2_min_trend
# sch_major_3_id
# sch_major_3_min_mean
# sch_major_3_min_std
# sch_major_3_min_trend

# major_1_id
# major_1_min_mean
# major_1_min_std
# major_1_min_trend
# major_2_id
# major_2_min_mean
# major_2_min_std
# major_2_min_trend
# major_3_id
# major_3_min_mean
# major_3_min_std
# major_3_min_trend


# python manage.py shell < /Users/kunyue/project_personal/my_project/mysite/gaokao/processor/model.py

class Model(object):

    # 这个模型是为了得到每个大学在当年录取的时候，每个专业的预测分
    def rule_model(self, academic_year='2019'):
        from gaokao.models import School, ModelRuleResult
        import sqlite3
        import pandas as pd
        import numpy
        # Create your connection.
        cnx = sqlite3.connect('db.sqlite3')

        df_sch_major = pd.read_sql_query("SELECT * FROM gaokao_schoolmajor where academic_year=" + academic_year + "",
                                         cnx)
        df_major_split = pd.read_sql_query("SELECT * FROM gaokao_majorsplit", cnx)
        df_sch_major_score = pd.read_sql_query("SELECT * FROM gaokao_schoolmajorsplit", cnx)

        df_sch_major_score = df_sch_major_score[
            (df_sch_major_score['min_score_diff_mean'] >= 0) &
            (df_sch_major_score['min_score_rank_mean'] >= 0) &
            (df_sch_major_score['min_score_diff_std'] >= 0) &
            (df_sch_major_score['min_score_rank_std'] >= 0) &
            (df_sch_major_score['avg_score_diff_mean'] >= 0) &
            (df_sch_major_score['avg_score_rank_mean'] >= 0) &
            (df_sch_major_score['avg_score_diff_std'] >= 0) &
            (df_sch_major_score['avg_score_rank_std'] >= 0)
            ]

        df_sch_major_split = pd.merge(df_sch_major, df_major_split, left_on='enroll_major_name', right_on='major_name')
        df_sch_major_split_3 = df_sch_major_split[
            ['school_id', 'wenli', 'batch_name', 'province_id', 'enroll_major_name', 'mname', 'enroll_major_id']]
        df_sch_major_split_3 = df_sch_major_split_3[df_sch_major_split_3['mname'].map(lambda x: len(str(x)) >= 1)]
        df_sch_major_split_3['m_level'] = 3

        df_sch_major_split_2 = df_sch_major_split[
            ['school_id', 'wenli', 'batch_name', 'province_id', 'enroll_major_name', 'cname',
             'enroll_major_id']].rename(
            columns={
                'cname': 'mname'
            }
        )
        df_sch_major_split_2 = df_sch_major_split_2[df_sch_major_split_2['mname'].map(lambda x: len(str(x)) >= 1)]
        df_sch_major_split_2['m_level'] = 2

        df_sch_major_split_1 = df_sch_major_split[
            ['school_id', 'wenli', 'batch_name', 'province_id', 'enroll_major_name', 'sname',
             'enroll_major_id']].rename(
            columns={
                'sname': 'mname'
            }
        )
        df_sch_major_split_1 = df_sch_major_split_1[df_sch_major_split_1['mname'].map(lambda x: len(str(x)) >= 1)]
        df_sch_major_split_1['m_level'] = 1

        df_sch_major_split_merge = pd.concat([df_sch_major_split_3, df_sch_major_split_2, df_sch_major_split_1])
        df_sch_major_score = df_sch_major_score[
            ['school_id', 'wenli', 'batch_name', 'province_id', 'mname', 'm_level',
             'min_score_diff_mean',
             'min_score_rank_mean',
             'min_score_diff_std',
             'min_score_rank_std',
             'avg_score_diff_mean',
             'avg_score_rank_mean',
             'avg_score_diff_std',
             'avg_score_rank_std',
             ]]
        df_sch_major_score_merge = pd.merge(df_sch_major_split_merge, df_sch_major_score,
                                            on=['school_id', 'wenli', 'batch_name', 'province_id', 'mname', 'm_level'])

        def weight_cal(x):
            if x == 3:
                return 0.6
            elif x == 2:
                return 0.3
            else:
                return 0.1

        df_sch_major_score_merge['weight'] = df_sch_major_score_merge['m_level'].map(weight_cal)

        def my_agg(x):

            # d = {}
            # d['a_sum'] = x['a'].sum()
            # d['a_max'] = x['a'].max()
            # d['b_mean'] = x['b'].mean()
            # d['c_d_prodsum'] = (x['c'] * x['d']).sum()
            # return pd.Series(d, index=['a_sum', 'a_max', 'b_mean', 'c_d_prodsum'])

            names = {
                'min_score_diff_mean': (x['min_score_diff_mean'] * x['weight']).sum() / x['weight'].sum(),
                'min_score_diff_std': (x['min_score_diff_std'] * x['weight']).sum() / x['weight'].sum(),
                'min_score_rank_mean': (x['min_score_rank_mean'] * x['weight']).sum() / x['weight'].sum(),
                'min_score_rank_std': (x['min_score_rank_std'] * x['weight']).sum() / x['weight'].sum(),
                'avg_score_diff_mean': (x['avg_score_diff_mean'] * x['weight']).sum() / x['weight'].sum(),
                'avg_score_diff_std': (x['avg_score_diff_std'] * x['weight']).sum() / x['weight'].sum(),
                'avg_score_rank_mean': (x['avg_score_rank_mean'] * x['weight']).sum() / x['weight'].sum(),
                'avg_score_rank_std': (x['avg_score_rank_std'] * x['weight']).sum() / x['weight'].sum()
            }
            return pd.Series(names,
                             [
                                 'min_score_diff_mean',
                                 'min_score_diff_std',
                                 'min_score_rank_mean',
                                 'min_score_rank_std',
                                 'avg_score_diff_mean',
                                 'avg_score_diff_std',
                                 'avg_score_rank_mean',
                                 'avg_score_rank_std'
                             ])

        result_merge_grp = df_sch_major_score_merge.groupby(
            ['school_id', 'wenli', 'batch_name', 'province_id', 'enroll_major_name', 'enroll_major_id']).apply(
            my_agg).reset_index()
        #
        #
        # # result_merge_grp.to_excel('/Users/kunyue/project_personal/my_project/mysite/data/dataxxx.xlsx')
        list_result = []
        for index, row in result_merge_grp.iterrows():
            kargs = {}
            kargs['enroll_major_id'] = row['enroll_major_id']
            kargs['enroll_major_name'] = row['enroll_major_name']
            kargs['batch_name'] = row['batch_name']
            kargs['wenli'] = row['wenli']
            kargs['province_id'] = row['province_id']
            kargs['min_score_diff_mean'] = row['min_score_diff_mean']
            kargs['min_score_diff_std'] = row['min_score_diff_std']
            kargs['min_score_rank_mean'] = row['min_score_rank_mean']
            kargs['min_score_rank_std'] = row['min_score_rank_std']
            kargs['avg_score_diff_mean'] = row['avg_score_diff_mean']
            kargs['avg_score_diff_std'] = row['avg_score_diff_std']
            kargs['avg_score_rank_mean'] = row['avg_score_rank_mean']
            kargs['avg_score_rank_std'] = row['avg_score_rank_std']

            school = School.objects.get(sch_id=row['school_id'])
            list_result.append(ModelRuleResult(**kargs, school=school))

        ModelRuleResult.objects.bulk_create(list_result)

    def fea_generate(self):
        pass


md = Model()
md.rule_model('2019')
