# variable req file would look something like this...
# list of expected values for key variables in the dataset

expected_column_values = {
    "event_type": ['pricing_page', 'form_submit',
                   'demo_click', 'whitepaper_download',
                   'page_view', 'scroll', 'click', 'exit'],
    "persona_type": ['researcher', 'buyer_intent', 'curious', 'demo_seeker']
}

# funnel creation 

HIGH = ['behavior_total_pages_viewed_gt_10', 'behavior_session_length_gt_15min', 'behavior_downloaded_paper',
        'refer_organic_search', 'campaign_was_retargeted', 'email_company', 'page_visit_security']

MEDIUM = ['behavior_used_search_feature', 'behavior_is_return_visitor',
          'refer_linkedin', 'campaign_utm_campaign_q2_data_lake_series', 'campaign_was_targeted_abm',
          'device_type_desktop',
          'page_visit_feature_compare', 'ip_us']

LOW = ['page_visit_case_study', 'refer_medium_tech_blog', 'page_visit_careers']

# user creation 
funnel_choices = ['top', 'middle', 'bottom']
funnel_weights = [0.5, 0.4, 0.1]
conversion_probs = {'top': 0.05, 'middle': 0.30, 'bottom': 0.80}

# model specifications
features = [
'behavior_total_pages_viewed_gt_10', 'behavior_session_length_gt_15min', 'behavior_downloaded_paper',
        'refer_organic_search', 'campaign_was_retargeted', 'email_company', 'page_visit_security',
'behavior_used_search_feature', 'behavior_is_return_visitor',
          'refer_linkedin', 'campaign_utm_campaign_q2_data_lake_series', 'campaign_was_targeted_abm',
          'device_type_desktop',
          'page_visit_feature_compare', 'ip_us',
'page_visit_case_study', 'refer_medium_tech_blog', 'page_visit_careers']
