# main entry point
# meant to mimic what would happen in a larger pipeline or orchestration system

import json

import data_generator as dg
import event_tracker as et
# import input_tests as it # example data checks
import stats_calculator as sc
import model_maker as mm


# create data
user_json = dg.generate_users(n=1000, start_date="2025-05-21", end_date="2025-05-22")
print(json.dumps(user_json['user_id_0'], indent=4))

# capture all data
views_df = et.track_view(user_json)

# run data tests
print(views_df.head())
# it.check_nulls(views_df)
# etc etc

# capture book_demo data
book_demo_df = et.track_book_demo(views_df)

# run stats
views = sc.get_views_last_24hr(views_df)
print(views)
demos = sc.get_demos_last_24hr(book_demo_df)
print(demos)

# these checks would exist in a separate workflow
# checks function working as intended
test_avg1 = sc.moving_average_views(df=views_df, duration=1)
print(test_avg1)
test_avg10 = sc.moving_average_views(df=views_df, duration=10)
print(test_avg10)
test_avg30 = sc.moving_average_views(df=views_df, duration=30)
print(test_avg30) # throws error as intended

# checks
test_avg_attr0 = sc.moving_average_views_query(df=views_df, duration=2, attribute_filter=('behavior_total_pages_viewed_gt_10', True))
test_avg_attr1 = sc.moving_average_views_query(df=views_df, duration=2, attribute_filter=('behavior_total_pages_viewed_gt_10', False))
print(test_avg_attr0)
print(test_avg_attr1)

# make the model

# to do: move this into an input file
features = [
'behavior_total_pages_viewed_gt_10', 'behavior_session_length_gt_15min', 'behavior_downloaded_paper',
        'refer_organic_search', 'campaign_was_retargeted', 'email_company', 'page_visit_security',
'behavior_used_search_feature', 'behavior_is_return_visitor',
          'refer_linkedin', 'campaign_utm_campaign_q2_data_lake_series', 'campaign_was_targeted_abm',
          'device_type_desktop',
          'page_visit_feature_compare', 'ip_us',
'page_visit_case_study', 'refer_medium_tech_blog', 'page_visit_careers']

model = mm.run_logistic_regression(df=views_df, target='book_demo', list_of_features=features)

