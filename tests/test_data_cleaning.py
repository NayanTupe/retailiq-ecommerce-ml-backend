import pandas as pd

from src.data.data_cleaning import clean_column_names, clean_data


def test_clean_column_names():
    sample_df = pd.DataFrame(
        {
            "Customer ID": [1, 2],
            "Total Spend": [100.0, 200.0],
            "Average Rating": [4.5, 3.8]
        }
    )

    cleaned_df = clean_column_names(sample_df)

    expected_columns = [
        "customer_id",
        "total_spend",
        "average_rating"
    ]

    assert cleaned_df.columns.tolist() == expected_columns


def test_clean_data_removes_duplicates():
    sample_df = pd.DataFrame(
        {
            "Customer_ID": [1, 1, 2],
            "Gender": ["Male", "Male", "Female"],
            "Age": [30, 30, 25],
            "City": ["Miami", "Miami", "Chicago"],
            "Membership_Type": ["Bronze", "Bronze", "Gold"],
            "Total_Spend": [200.0, 200.0, 500.0],
            "Items_Purchased": [4, 4, 10],
            "Average_Rating": [3.5, 3.5, 4.5],
            "Discount_Applied": [True, True, False],
            "Days_Since_Last_Purchase": [20, 20, 10],
            "Satisfaction_Level": ["Neutral", "Neutral", "Satisfied"]
        }
    )

    cleaned_df = clean_data(sample_df)

    assert cleaned_df.duplicated().sum() == 0
    assert cleaned_df.shape[0] == 2


def test_clean_data_validates_numeric_ranges():
    sample_df = pd.DataFrame(
        {
            "Customer_ID": [1, 2, 3],
            "Gender": ["Male", "Female", "Male"],
            "Age": [30, 150, 25],
            "City": ["Miami", "Chicago", "Houston"],
            "Membership_Type": ["Bronze", "Gold", "Silver"],
            "Total_Spend": [200.0, 500.0, -50.0],
            "Items_Purchased": [4, 10, 3],
            "Average_Rating": [3.5, 4.5, 6.0],
            "Discount_Applied": [True, False, True],
            "Days_Since_Last_Purchase": [20, 10, 30],
            "Satisfaction_Level": ["Neutral", "Satisfied", "Unsatisfied"]
        }
    )

    cleaned_df = clean_data(sample_df)

    assert cleaned_df.shape[0] == 1
    assert cleaned_df.iloc[0]["customer_id"] == 1