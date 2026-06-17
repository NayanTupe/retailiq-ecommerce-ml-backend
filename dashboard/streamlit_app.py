import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="RetailIQ | E-commerce Intelligence",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ======================================================
# CUSTOM PREMIUM CSS
# ======================================================

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(59, 130, 246, 0.22), transparent 30%),
                radial-gradient(circle at top right, rgba(168, 85, 247, 0.20), transparent 28%),
                linear-gradient(135deg, #f8fbff 0%, #eef4ff 45%, #f7f0ff 100%);
        }

        .block-container {
            padding-top: 1.3rem;
            padding-bottom: 2.5rem;
            max-width: 1550px;
        }

        section[data-testid="stSidebar"] {
            background:
                linear-gradient(180deg, #07111f 0%, #0f172a 48%, #111827 100%);
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        section[data-testid="stSidebar"] * {
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] span {
            color: #0f172a !important;
        }

        section[data-testid="stSidebar"] input {
            color: #0f172a !important;
        }

        .sidebar-brand {
            padding: 18px 14px 18px 14px;
            border-radius: 22px;
            background:
                linear-gradient(135deg, rgba(37,99,235,0.35), rgba(168,85,247,0.25));
            border: 1px solid rgba(255,255,255,0.14);
            box-shadow: 0 18px 40px rgba(0,0,0,0.25);
            margin-bottom: 18px;
        }

        .sidebar-title {
            font-size: 28px;
            font-weight: 900;
            letter-spacing: -0.8px;
            margin-bottom: 4px;
        }

        .sidebar-subtitle {
            font-size: 13px;
            color: #cbd5e1 !important;
            line-height: 1.5;
        }

        .hero {
            position: relative;
            overflow: hidden;
            padding: 40px 42px;
            border-radius: 34px;
            background:
                linear-gradient(135deg, #061226 0%, #123b8f 45%, #7c3aed 100%);
            box-shadow:
                0 28px 70px rgba(15, 23, 42, 0.30),
                inset 0 1px 0 rgba(255,255,255,0.22);
            color: white;
            margin-bottom: 26px;
        }

        .hero:before {
            content: "";
            position: absolute;
            width: 420px;
            height: 420px;
            right: -130px;
            top: -160px;
            background: radial-gradient(circle, rgba(255,255,255,0.25), transparent 65%);
            border-radius: 50%;
        }

        .hero:after {
            content: "";
            position: absolute;
            width: 220px;
            height: 220px;
            left: 55%;
            bottom: -120px;
            background: radial-gradient(circle, rgba(34,211,238,0.32), transparent 70%);
            border-radius: 50%;
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .hero-badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.22);
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 16px;
            backdrop-filter: blur(14px);
        }

        .hero-title {
            font-size: 48px;
            line-height: 1.05;
            font-weight: 950;
            letter-spacing: -1.8px;
            margin-bottom: 16px;
        }

        .hero-title span {
            color: #93c5fd;
        }

        .hero-subtitle {
            font-size: 17px;
            line-height: 1.75;
            color: #dbeafe;
            max-width: 960px;
            margin-bottom: 22px;
        }

        .hero-tags {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .hero-tag {
            padding: 9px 14px;
            border-radius: 999px;
            background: rgba(255,255,255,0.13);
            border: 1px solid rgba(255,255,255,0.18);
            font-size: 13px;
            font-weight: 700;
            backdrop-filter: blur(10px);
        }

        .kpi-card {
            position: relative;
            overflow: hidden;
            background: rgba(255,255,255,0.82);
            backdrop-filter: blur(18px);
            border: 1px solid rgba(255,255,255,0.78);
            border-radius: 28px;
            padding: 25px 25px;
            min-height: 165px;
            box-shadow:
                0 20px 45px rgba(15,23,42,0.10),
                inset 0 1px 0 rgba(255,255,255,0.9);
            transition: all 0.28s ease;
        }

        .kpi-card:hover {
            transform: translateY(-6px);
            box-shadow:
                0 28px 70px rgba(15,23,42,0.16),
                inset 0 1px 0 rgba(255,255,255,0.95);
        }

        .kpi-card:before {
            content: "";
            position: absolute;
            width: 120px;
            height: 120px;
            right: -35px;
            top: -35px;
            border-radius: 50%;
            background: var(--accent);
            opacity: 0.16;
        }

        .kpi-icon {
            width: 44px;
            height: 44px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--accent);
            color: white;
            font-size: 21px;
            margin-bottom: 16px;
            box-shadow: 0 12px 25px rgba(15,23,42,0.18);
        }

        .kpi-label {
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: #64748b;
            font-weight: 800;
            margin-bottom: 8px;
        }

        .kpi-value {
            font-size: 32px;
            color: #0f172a;
            font-weight: 950;
            letter-spacing: -1px;
            margin-bottom: 8px;
        }

        .kpi-note {
            font-size: 13px;
            color: #475569;
            font-weight: 600;
        }

        .section-title {
            margin-top: 8px;
            margin-bottom: 6px;
            font-size: 29px;
            font-weight: 950;
            letter-spacing: -0.8px;
            color: #0f172a;
        }

        .section-subtitle {
            font-size: 15px;
            color: #64748b;
            margin-bottom: 21px;
            line-height: 1.6;
        }

        .chart-card {
            background: rgba(255,255,255,0.86);
            border-radius: 28px;
            padding: 18px;
            border: 1px solid rgba(255,255,255,0.8);
            box-shadow: 0 18px 45px rgba(15,23,42,0.08);
            margin-bottom: 18px;
        }

        .insight-card {
            background: rgba(255,255,255,0.86);
            backdrop-filter: blur(18px);
            border: 1px solid rgba(255,255,255,0.8);
            border-radius: 28px;
            padding: 26px;
            box-shadow: 0 20px 50px rgba(15,23,42,0.09);
            margin-bottom: 18px;
            transition: 0.25s ease;
        }

        .insight-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 28px 65px rgba(15,23,42,0.14);
        }

        .insight-title {
            font-size: 19px;
            font-weight: 900;
            color: #0f172a;
            margin-bottom: 10px;
        }

        .insight-text {
            font-size: 14px;
            color: #475569;
            line-height: 1.8;
        }

        .pill {
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 800;
            margin-top: 10px;
        }

        .pill-red {
            background: #fee2e2;
            color: #b91c1c;
        }

        .pill-yellow {
            background: #fef3c7;
            color: #92400e;
        }

        .pill-green {
            background: #dcfce7;
            color: #166534;
        }

        .risk-high {
            color: #dc2626;
            font-weight: 950;
        }

        .risk-medium {
            color: #d97706;
            font-weight: 950;
        }

        .risk-low {
            color: #16a34a;
            font-weight: 950;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 12px;
            background: rgba(255,255,255,0.55);
            padding: 10px;
            border-radius: 24px;
            border: 1px solid rgba(255,255,255,0.75);
            box-shadow: 0 14px 35px rgba(15,23,42,0.06);
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 18px;
            padding: 13px 20px;
            font-weight: 850;
            color: #334155;
        }

        .stTabs [aria-selected="true"] {
            background:
                linear-gradient(135deg, #2563eb, #7c3aed) !important;
            color: white !important;
            box-shadow: 0 14px 30px rgba(37,99,235,0.30);
        }

        div[data-testid="stDataFrame"] {
            border-radius: 22px;
            overflow: hidden;
            box-shadow: 0 18px 40px rgba(15,23,42,0.08);
        }

        .stButton > button {
            background: linear-gradient(135deg, #2563eb, #7c3aed);
            color: white;
            border: none;
            border-radius: 18px;
            padding: 0.8rem 1.2rem;
            font-weight: 850;
            box-shadow: 0 15px 35px rgba(37,99,235,0.30);
            transition: 0.25s ease;
        }

        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 22px 45px rgba(37,99,235,0.38);
            color: white;
        }

        .footer {
            margin-top: 28px;
            padding: 22px;
            text-align: center;
            color: #64748b;
            font-size: 14px;
            font-weight: 600;
        }

        @media only screen and (max-width: 900px) {
            .hero {
                padding: 30px 24px;
                border-radius: 26px;
            }

            .hero-title {
                font-size: 34px;
            }

            .hero-subtitle {
                font-size: 15px;
            }

            .kpi-value {
                font-size: 25px;
            }

            .section-title {
                font-size: 24px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ======================================================
# PATHS
# ======================================================

SEGMENTED_DATA_PATH = Path("data/processed/customer_segments.csv")
FEATURE_DATA_PATH = Path("data/processed/final_features.csv")


# ======================================================
# DATA
# ======================================================

@st.cache_data
def load_data():
    if SEGMENTED_DATA_PATH.exists():
        return pd.read_csv(SEGMENTED_DATA_PATH)

    if FEATURE_DATA_PATH.exists():
        return pd.read_csv(FEATURE_DATA_PATH)

    raise FileNotFoundError(
        "Processed data not found. Run feature engineering and segmentation first."
    )


# ======================================================
# HELPERS
# ======================================================

def money(value):
    return f"${value:,.2f}"


def section_header(title, subtitle):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-subtitle'>{subtitle}</div>", unsafe_allow_html=True)


def kpi_card(icon, label, value, note, color):
    st.markdown(
        f"""
        <div class="kpi-card" style="--accent:{color};">
            <div class="kpi-icon">{icon}</div>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def wrap_chart(fig):
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        font=dict(family="Inter", color="#334155"),
        title=dict(font=dict(size=18, color="#0f172a")),
        margin=dict(l=30, r=25, t=65, b=35),
        legend=dict(
            bgcolor="rgba(255,255,255,0)",
            font=dict(size=12)
        )
    )
    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


def sidebar_filters(df):
    st.sidebar.markdown(
        """
        <div class="sidebar-brand">
            <div class="sidebar-title">RetailIQ</div>
            <div class="sidebar-subtitle">
                Premium customer analytics, churn intelligence and segmentation dashboard.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("### Filters")

    membership_values = sorted(df["membership_type"].unique())
    city_values = sorted(df["city"].unique())
    gender_values = sorted(df["gender"].unique())

    selected_memberships = st.sidebar.multiselect(
        "Membership Type",
        membership_values,
        default=membership_values
    )

    selected_cities = st.sidebar.multiselect(
        "City",
        city_values,
        default=city_values
    )

    selected_genders = st.sidebar.multiselect(
        "Gender",
        gender_values,
        default=gender_values
    )

    age_min = int(df["age"].min())
    age_max = int(df["age"].max())

    selected_age = st.sidebar.slider(
        "Age Range",
        min_value=age_min,
        max_value=age_max,
        value=(age_min, age_max)
    )

    spend_min = float(df["total_spend"].min())
    spend_max = float(df["total_spend"].max())

    selected_spend = st.sidebar.slider(
        "Spend Range",
        min_value=spend_min,
        max_value=spend_max,
        value=(spend_min, spend_max)
    )

    filtered = df[
        (df["membership_type"].isin(selected_memberships)) &
        (df["city"].isin(selected_cities)) &
        (df["gender"].isin(selected_genders)) &
        (df["age"].between(selected_age[0], selected_age[1])) &
        (df["total_spend"].between(selected_spend[0], selected_spend[1]))
    ]

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### Selected Customers")
    st.sidebar.markdown(f"## {len(filtered):,}")

    return filtered


# ======================================================
# UI SECTIONS
# ======================================================

def hero():
    st.markdown(
        """
        <div class="hero">
            <div class="hero-content">
                <div class="hero-badge">🛍️ E-commerce ML Portfolio Project</div>
                <div class="hero-title">
                    RetailIQ <span>Customer Intelligence</span> Dashboard
                </div>
                <div class="hero-subtitle">
                    A premium analytics platform for business owners to understand customer behavior,
                    revenue patterns, churn risk, customer segments and retention opportunities.
                </div>
                <div class="hero-tags">
                    <div class="hero-tag">Churn Prediction</div>
                    <div class="hero-tag">Customer Segmentation</div>
                    <div class="hero-tag">Revenue Analytics</div>
                    <div class="hero-tag">Business Insights</div>
                    <div class="hero-tag">Streamlit + ML</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def kpis(df):
    total_customers = df["customer_id"].nunique()
    total_revenue = df["total_spend"].sum()
    avg_spend = df["total_spend"].mean()
    churn_rate = df["churn"].mean() * 100

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card("👥", "Total Customers", f"{total_customers:,}", "Customers after filters", "#2563eb")

    with col2:
        kpi_card("💰", "Total Revenue", money(total_revenue), "Total spend generated", "#16a34a")

    with col3:
        kpi_card("🛒", "Average Spend", money(avg_spend), "Spend per customer", "#7c3aed")

    with col4:
        kpi_card("⚠️", "Churn Rate", f"{churn_rate:.2f}%", "Customers at risk", "#dc2626")


def overview_tab(df):
    section_header(
        "Executive Overview",
        "A clean summary of customer distribution, revenue contribution and membership performance."
    )

    col1, col2 = st.columns([1.35, 1])

    with col1:
        city_revenue = (
            df.groupby("city")["total_spend"]
            .sum()
            .reset_index()
            .sort_values("total_spend", ascending=False)
        )

        fig = px.bar(
            city_revenue,
            x="city",
            y="total_spend",
            title="Revenue by City",
            text_auto=".2s",
            color="total_spend",
            color_continuous_scale=["#93c5fd", "#2563eb", "#1e3a8a"]
        )
        fig.update_layout(height=430, showlegend=False)
        wrap_chart(fig)

    with col2:
        membership_data = df["membership_type"].value_counts().reset_index()
        membership_data.columns = ["membership_type", "customers"]

        fig = px.pie(
            membership_data,
            names="membership_type",
            values="customers",
            title="Membership Mix",
            hole=0.58,
            color_discrete_sequence=["#2563eb", "#7c3aed", "#22c55e", "#f97316"]
        )
        fig.update_layout(height=430)
        wrap_chart(fig)

    col3, col4 = st.columns(2)

    with col3:
        age_fig = px.histogram(
            df,
            x="age",
            nbins=25,
            title="Customer Age Distribution",
            color_discrete_sequence=["#7c3aed"]
        )
        age_fig.update_layout(height=390)
        wrap_chart(age_fig)

    with col4:
        rating_membership = (
            df.groupby("membership_type")["average_rating"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            rating_membership,
            x="membership_type",
            y="average_rating",
            title="Average Rating by Membership",
            text_auto=".2f",
            color="average_rating",
            color_continuous_scale=["#fecaca", "#facc15", "#22c55e"]
        )
        fig.update_layout(height=390, showlegend=False)
        wrap_chart(fig)


def churn_tab(df):
    section_header(
        "Churn Intelligence",
        "Identify churn patterns by membership, city, rating behavior and discount usage."
    )

    churn_data = df["churn"].value_counts().reset_index()
    churn_data.columns = ["churn", "customers"]
    churn_data["status"] = churn_data["churn"].map({0: "No Churn", 1: "Churn Risk"})

    col1, col2 = st.columns([1, 1.25])

    with col1:
        fig = px.pie(
            churn_data,
            names="status",
            values="customers",
            title="Overall Churn Distribution",
            hole=0.62,
            color="status",
            color_discrete_map={
                "No Churn": "#22c55e",
                "Churn Risk": "#ef4444"
            }
        )
        fig.update_layout(height=430)
        wrap_chart(fig)

    with col2:
        churn_membership = (
            df.groupby("membership_type")["churn"]
            .mean()
            .reset_index()
        )
        churn_membership["churn_rate"] = churn_membership["churn"] * 100

        fig = px.bar(
            churn_membership,
            x="membership_type",
            y="churn_rate",
            title="Churn Rate by Membership Type",
            text_auto=".2f",
            color="churn_rate",
            color_continuous_scale=["#bbf7d0", "#fde68a", "#ef4444"]
        )
        fig.update_layout(height=430, showlegend=False)
        wrap_chart(fig)

    col3, col4 = st.columns(2)

    with col3:
        churn_city = (
            df.groupby("city")["churn"]
            .mean()
            .reset_index()
            .sort_values("churn", ascending=False)
        )
        churn_city["churn_rate"] = churn_city["churn"] * 100

        fig = px.bar(
            churn_city,
            x="city",
            y="churn_rate",
            title="Churn Rate by City",
            text_auto=".2f",
            color="churn_rate",
            color_continuous_scale=["#bfdbfe", "#facc15", "#dc2626"]
        )
        fig.update_layout(height=400, showlegend=False)
        wrap_chart(fig)

    with col4:
        rating_churn = (
            df.groupby("low_rating_flag")["churn"]
            .mean()
            .reset_index()
        )
        rating_churn["rating_group"] = rating_churn["low_rating_flag"].map({
            0: "Normal Rating",
            1: "Low Rating"
        })
        rating_churn["churn_rate"] = rating_churn["churn"] * 100

        fig = px.bar(
            rating_churn,
            x="rating_group",
            y="churn_rate",
            title="Churn Rate by Rating Quality",
            text_auto=".2f",
            color="churn_rate",
            color_continuous_scale=["#22c55e", "#facc15", "#ef4444"]
        )
        fig.update_layout(height=400, showlegend=False)
        wrap_chart(fig)


def segment_tab(df):
    section_header(
        "Customer Segmentation",
        "Customer groups created using K-Means clustering for targeted business actions."
    )

    if "segment_name" not in df.columns:
        st.warning("Segmentation data not found. Run train_segmentation_model.py first.")
        return

    segment_summary = (
        df.groupby("segment_name")
        .agg(
            customers=("customer_id", "count"),
            revenue=("total_spend", "sum"),
            avg_spend=("total_spend", "mean"),
            avg_items=("items_purchased", "mean"),
            avg_rating=("average_rating", "mean"),
            churn_rate=("churn", "mean")
        )
        .reset_index()
    )

    segment_summary["churn_rate"] = segment_summary["churn_rate"] * 100

    col1, col2 = st.columns(2)

    with col1:
        fig = px.treemap(
            segment_summary,
            path=["segment_name"],
            values="customers",
            color="churn_rate",
            title="Customer Segment Size and Risk",
            color_continuous_scale=["#22c55e", "#facc15", "#ef4444"]
        )
        fig.update_layout(height=450)
        wrap_chart(fig)

    with col2:
        fig = px.scatter(
            segment_summary,
            x="avg_spend",
            y="churn_rate",
            size="customers",
            color="segment_name",
            title="Segment Spend vs Churn Risk Matrix",
            size_max=70,
            color_discrete_sequence=["#ef4444", "#2563eb", "#f97316", "#7c3aed"]
        )
        fig.update_layout(height=450)
        wrap_chart(fig)

    col3, col4 = st.columns(2)

    with col3:
        fig = px.bar(
            segment_summary.sort_values("revenue", ascending=False),
            x="segment_name",
            y="revenue",
            title="Revenue Contribution by Segment",
            text_auto=".2s",
            color="revenue",
            color_continuous_scale=["#bfdbfe", "#2563eb", "#1e3a8a"]
        )
        fig.update_layout(height=420, showlegend=False)
        wrap_chart(fig)

    with col4:
        fig = px.bar(
            segment_summary.sort_values("churn_rate", ascending=False),
            x="segment_name",
            y="churn_rate",
            title="Churn Rate by Segment",
            text_auto=".2f",
            color="churn_rate",
            color_continuous_scale=["#bbf7d0", "#facc15", "#dc2626"]
        )
        fig.update_layout(height=420, showlegend=False)
        wrap_chart(fig)

    st.markdown("### Segment Summary Table")
    st.dataframe(segment_summary.round(2), use_container_width=True, hide_index=True)


def predictor_tab():
    section_header(
        "Smart Churn Risk Predictor",
        "A polished business form to estimate customer churn risk and suggest retention actions."
    )

    st.markdown(
        """
        <div class="insight-card">
            <div class="insight-title">How this works</div>
            <div class="insight-text">
                This dashboard predictor uses business risk scoring for instant owner-level decisions.
                The production ML model/API integration will be added in the FastAPI phase.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.slider("Age", 18, 80, 32)
        city = st.selectbox(
            "City",
            ["New York", "Los Angeles", "Chicago", "Houston", "Miami", "San Francisco"]
        )

    with col2:
        membership = st.selectbox("Membership Type", ["Bronze", "Silver", "Gold"])
        total_spend = st.number_input("Total Spend", min_value=0.0, value=250.0)
        items_purchased = st.number_input("Items Purchased", min_value=1, value=4)

    with col3:
        average_rating = st.slider("Average Rating", 1.0, 5.0, 3.0, 0.1)
        discount_applied = st.selectbox("Discount Applied", ["Yes", "No"])
        days_since_last_purchase = st.slider("Days Since Last Purchase", 0, 120, 45)

    if st.button("Analyze Customer Risk", use_container_width=True):
        score = 0

        if days_since_last_purchase >= 45:
            score += 35
        if average_rating < 3:
            score += 25
        if membership == "Bronze":
            score += 15
        if total_spend < 250:
            score += 10
        if items_purchased <= 3:
            score += 10
        if discount_applied == "Yes":
            score += 5

        score = min(score, 100)

        if score >= 70:
            risk = "High Risk"
            css = "risk-high"
            pill = "pill-red"
            action = "Offer retention discount, loyalty reward, and personal follow-up."
        elif score >= 40:
            risk = "Medium Risk"
            css = "risk-medium"
            pill = "pill-yellow"
            action = "Send personalized offers and monitor customer engagement."
        else:
            risk = "Low Risk"
            css = "risk-low"
            pill = "pill-green"
            action = "Maintain regular communication and loyalty benefits."

        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-title">Prediction Result</div>
                <div class="insight-text">
                    Customer churn risk score is <b>{score}%</b>.<br/>
                    Risk Level: <span class="{css}">{risk}</span><br/>
                    <span class="pill {pill}">{risk}</span>
                    <br/><br/>
                    <b>Recommended Action:</b> {action}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


def insights_tab(df):
    section_header(
        "Owner-Level Business Insights",
        "Clear actions for retention, revenue growth, customer satisfaction and marketing campaigns."
    )

    churn_rate = df["churn"].mean() * 100
    avg_rating = df["average_rating"].mean()
    avg_spend = df["total_spend"].mean()

    if "segment_name" in df.columns:
        risky_segment = (
            df.groupby("segment_name")["churn"]
            .mean()
            .sort_values(ascending=False)
            .index[0]
        )
        best_segment = (
            df.groupby("segment_name")["total_spend"]
            .mean()
            .sort_values(ascending=False)
            .index[0]
        )
    else:
        risky_segment = "Churn Risk Customers"
        best_segment = "High Value Customers"

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-title">⚠️ Retention Priority</div>
                <div class="insight-text">
                    Current churn risk is <b>{churn_rate:.2f}%</b>.
                    Focus first on <b>{risky_segment}</b> because this group has the highest churn risk.
                </div>
                <span class="pill pill-red">High Priority</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-title">⭐ Satisfaction Opportunity</div>
                <div class="insight-text">
                    Average rating is <b>{avg_rating:.2f}</b>.
                    Low-rating customers should receive support follow-ups and feedback campaigns.
                </div>
                <span class="pill pill-yellow">Improve Experience</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-title">💰 Revenue Protection</div>
                <div class="insight-text">
                    Average spend per customer is <b>{money(avg_spend)}</b>.
                    Protect <b>{best_segment}</b> using loyalty rewards and premium communication.
                </div>
                <span class="pill pill-green">Protect Revenue</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="insight-card">
                <div class="insight-title">🚀 Growth Strategy</div>
                <div class="insight-text">
                    Convert satisfied regular customers into high-value customers using membership upgrades,
                    bundles, personalized recommendations and targeted offers.
                </div>
                <span class="pill pill-green">Growth Opportunity</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Recommended Business Action Plan")

    plan = pd.DataFrame(
        {
            "Priority": [1, 2, 3, 4],
            "Customer Group": [
                "At Risk Customers",
                "Low Engagement Customers",
                "Satisfied Regular Customers",
                "High Value Customers"
            ],
            "Action": [
                "Retention offer, feedback call, service recovery",
                "Re-engagement campaign and product recommendations",
                "Membership upgrade and bundled offers",
                "Loyalty rewards and premium communication"
            ],
            "Goal": [
                "Reduce churn",
                "Increase repeat purchase",
                "Increase customer lifetime value",
                "Protect revenue"
            ]
        }
    )

    st.dataframe(plan, use_container_width=True, hide_index=True)


# ======================================================
# MAIN APP
# ======================================================

def main():
    df = load_data()
    filtered_df = sidebar_filters(df)

    hero()

    if filtered_df.empty:
        st.warning("No customers found for selected filters. Please change filter options.")
        return

    kpis(filtered_df)

    st.markdown("<br/>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Executive Overview",
            "Churn Intelligence",
            "Customer Segments",
            "Risk Predictor",
            "Business Insights"
        ]
    )

    with tab1:
        overview_tab(filtered_df)

    with tab2:
        churn_tab(filtered_df)

    with tab3:
        segment_tab(filtered_df)

    with tab4:
        predictor_tab()

    with tab5:
        insights_tab(filtered_df)

    st.markdown(
        """
        <div class="footer">
            RetailIQ | Premium E-commerce ML Dashboard | Built with Python, Streamlit, Plotly and Machine Learning
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()