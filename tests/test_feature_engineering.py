import pandas as pd

from src.features.feature_engineering import (
    create_churn_label,
    create_customer_features
)


def test_create_churn_label_for_inactive_customer():
    sample_df = pd.DataFrame(
        {
            "days_since_last_purchase": [50, 20],
            "satisfaction_level": ["Neutral", "Satisfied"]
        }
    )

    result_df = create_churn_label(sample_df)

    assert "churn" in result_df.columns
    assert result_df.loc[0, "churn"] == 1
    assert result_df.loc[1, "churn"] == 0


def test_create_churn_label_for_unsatisfied_customer():
    sample_df = pd.DataFrame(
        {
            "days_since_last_purchase": [10, 15],
            "satisfaction_level": ["Unsatisfied", "Satisfied"]
        }
    )

    result_df = create_churn_label(sample_df)

    assert result_df.loc[0, "churn"] == 1
    assert result_df.loc[1, "churn"] == 0


def test_create_customer_features():
    sample_df = pd.DataFrame(
        {
            "total_spend": [100.0, 500.0, 900.0, 1200.0],
            "items_purchased": [2, 5, 10, 20],
            "days_since_last_purchase": [10, 50, 20, 60],
            "average_rating": [4.5, 2.5, 3.5, 1.5],
            "discount_applied": [True, False, True, False]
        }
    )

    result_df = create_customer_features(sample_df)

    expected_columns = [
        "avg_spend_per_item",
        "is_high_value_customer",
        "is_frequent_buyer",
        "is_inactive_customer",
        "low_rating_flag",
        "discount_used_flag"
    ]

    for column in expected_columns:
        assert column in result_df.columns

    assert result_df.loc[0, "avg_spend_per_item"] == 50.0
    assert result_df.loc[1, "is_inactive_customer"] == 1
    assert result_df.loc[1, "low_rating_flag"] == 1
    assert result_df.loc[0, "discount_used_flag"] == 1