## Overview
This project simulates a simplified web analytics system for a SaaS company with a sales-driven go-to-market strategy. It includes synthetic data generation, event tracking, summary statistics, and a basic modeling pipeline.


## Core Components

Synthetic Data Generation: Simulates web user attributes and behaviors across funnel stages (top, middle, bottom).

Event Tracking: Collects and retains events with hourly granularity over a 24-hour window.

Statistics Engine: Computes views and demo counts, as well as moving averages by time or user segment.

Modeling: A basic logistic regression to identify attributes most predictive of demo requests.

## Design Notes

Customer & User Assumptions
This project simulates the behavior of a high-consideration B2B SaaS buyer. I imagined a company like Snowflake, where demos are required and contracts are large.  I approached this as a greenfield project with no legacy code or client onboarding constraints, and I deliberately kept the structure lightweight and functional to allow for rapid iteration. 

The dataset captures user actions on a marketing website, including page visits, session length, and referral source. High-intent behaviors (e.g., downloading a white paper, visiting the security page) are modeled to predict conversion likelihood, while lower-intent signals (e.g., career page views, tech blog referrals) are less predictive. Metadata like UTM parameters, device type, and company email are also used to simulate meaningful segmentation. See the tab “Data Generator” for more details. 

## Data & Code Design Choices
The generator produces synthetic data in a JSON format, mimicking what might be streamed from a tool like Kafka. This is then flattened for analysis in the track_view() function. While the original brief assumed clean data, I included examples of silent error checks, which would be common in a real-world pipeline.

This project is implemented using a function-oriented approach to prioritize readability and modularity. Functions are easier to port across codebases, unit test in isolation, and understand across mixed-language teams. While object-oriented design offers advantages for larger systems, a function-oriented approach is more practical for lightweight, iterative DS workflows.

## Recommendations
Upgrade fidelity: Convert binary flags like session_length_gt_15 into continuous variables for richer analysis.


Page-level insights: Segment conversion behavior by geography and content (e.g., European users + security page view). Use this to optimize the site’s layout and reduce low-performing content.
