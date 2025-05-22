# generates the data in three steps (see design notes)
# 1: Assign each persona a set of behaviors according to a rules engine
# 2: Generate sets of users according to the proportions assigned
# 3: then Assign each user a prob of outcome behavior

import random
from datetime import datetime, timedelta

# Step 1: assign personas (i.e., a customer's location on the funnel)
# To Do: move this to an input file
HIGH = ['behavior_total_pages_viewed_gt_10', 'behavior_session_length_gt_15min', 'behavior_downloaded_paper',
        'refer_organic_search', 'campaign_was_retargeted', 'email_company', 'page_visit_security']

MEDIUM = ['behavior_used_search_feature', 'behavior_is_return_visitor',
          'refer_linkedin', 'campaign_utm_campaign_q2_data_lake_series', 'campaign_was_targeted_abm',
          'device_type_desktop',
          'page_visit_feature_compare', 'ip_us']

LOW = ['page_visit_case_study', 'refer_medium_tech_blog', 'page_visit_careers']

# generate behavior mix based on simple rules
def assign_attributes(funnel_level):
    """
    Assigns boolean attributes based on funnel stage logic:
    - Top: only low-signal attributes
    - Middle: probabilistic mix of medium attributes
    - Bottom: guarantees one high-signal attribute, disables low
    """

    attributes = {attr: False for attr in HIGH + MEDIUM + LOW}  # start with all False

    if funnel_level == 'top':
        for attr in LOW:
            attributes[attr] = True
        # All medium and high = False (already defaulted to False)
        pass

    elif funnel_level == 'middle':
        for attr in MEDIUM:
            attributes[attr] = random.random() < 0.5

    elif funnel_level == 'bottom':
        high_attr = random.choice(HIGH)
        attributes[high_attr] = True  # ensure at least one high is True
        for attr in MEDIUM:
            attributes[attr] = random.random() < 0.5
        for attr in LOW:
            attributes[attr] = False

    return attributes


# Steps 2 and 3: generate the users according to the parameters specified

# To Do: move these to an input file
funnel_choices = ['top', 'middle', 'bottom']
funnel_weights = [0.5, 0.4, 0.1]
conversion_probs = {'top': 0.05, 'middle': 0.30, 'bottom': 0.80}


def generate_users(n=1000, start_date="2025-05-01", end_date="2025-05-21"):
    "doc string here"
    users = []

    # Convert to datetime objects
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")

    for i in range(n):
        funnel = random.choices(funnel_choices, weights=funnel_weights, k=1)[0]
        attrs = assign_attributes(funnel)
        book_demo = random.random() < conversion_probs[funnel]

        # Random timestamp in date range
        random_offset = timedelta(hours=random.randint(0, 23))
        timestamp = start_dt + random_offset

        users.append({
            "user_id": f"user_{i}",
            "timestamp": timestamp.isoformat(),  # ISO 8601 format
            "funnel": funnel,
            "book_demo": book_demo,
            **attrs
        })

    return users
