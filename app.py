import streamlit as st
import joblib
import numpy as np


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏡",
    layout="wide"
)


# =========================================================
# DEFAULT VALUES
# =========================================================

DEFAULT_VALUES = {
    "avg_income": 60000.0,
    "house_age": 5.0,
    "rooms": 6.0,
    "bedrooms": 3.0,
    "population": 35000.0
}


# =========================================================
# INITIALIZE SESSION STATE
# =========================================================

for key, value in DEFAULT_VALUES.items():

    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# RESET FUNCTION
# =========================================================

def reset_values():

    for key, value in DEFAULT_VALUES.items():
        st.session_state[key] = value


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN APP
       ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 5%,
                rgba(224, 231, 255, 0.85),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(219, 234, 254, 0.9),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #f8fafc 0%,
                #eef2ff 50%,
                #eff6ff 100%
            );
    }


    .block-container {
        max-width: 1100px;
        padding-top: 35px;
        padding-bottom: 25px;
    }


    /* =====================================================
       HEADER
       ===================================================== */

    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 850;
        color: #312e81;
        letter-spacing: -1.5px;
        margin-bottom: 5px;
    }


    .main-subtitle {
        text-align: center;
        color: #64748b;
        font-size: 17px;
        margin-bottom: 22px;
    }


    .status-box {
        width: fit-content;
        margin: 0 auto 32px auto;
        padding: 9px 20px;
        border-radius: 30px;

        background: rgba(255, 255, 255, 0.78);
        border: 1px solid rgba(148, 163, 184, 0.35);

        color: #475569;
        font-size: 14px;
        font-weight: 650;

        box-shadow:
            0 6px 20px rgba(15, 23, 42, 0.06);

        backdrop-filter: blur(10px);
    }


    /* =====================================================
       SECTION HEADINGS
       ===================================================== */

    .section-heading {
        font-size: 26px;
        font-weight: 800;
        color: #1e293b;
        margin-top: 10px;
        margin-bottom: 5px;
    }


    .section-text {
        color: #64748b;
        font-size: 15px;
        margin-bottom: 20px;
    }


    /* =====================================================
       INPUT BOXES
       ===================================================== */

    div[data-testid="stNumberInput"] {
        background: rgba(255, 255, 255, 0.82);

        border-radius: 15px;

        padding: 3px 6px;

        border: 1px solid rgba(203, 213, 225, 0.65);

        box-shadow:
            0 4px 14px rgba(15, 23, 42, 0.04);

        transition: 0.2s ease;
    }


    div[data-testid="stNumberInput"]:hover {
        border-color: #a5b4fc;

        box-shadow:
            0 7px 20px rgba(79, 70, 229, 0.08);
    }


    div[data-testid="stNumberInput"] input {
        font-weight: 600;
        color: #1e293b;
    }


    /* =====================================================
       ACTION BUTTON AREA
       ===================================================== */

    div[data-testid="stHorizontalBlock"] div.stButton {
        display: flex;
        justify-content: center;
    }


    /* =====================================================
       ALL BUTTONS
       ===================================================== */

    div.stButton > button {

        width: 100%;

        height: 58px;

        border-radius: 16px;

        font-size: 16px;

        font-weight: 750;

        letter-spacing: 0.2px;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease,
            background 0.2s ease,
            border-color 0.2s ease;

        box-shadow:
            0 7px 18px rgba(15, 23, 42, 0.08);
    }


    /* =====================================================
       PREDICT BUTTON
       ===================================================== */

    div.stButton > button[kind="primary"] {

        background: linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        );

        color: white;

        border: 1px solid rgba(255, 255, 255, 0.25);

        box-shadow:
            0 9px 25px rgba(79, 70, 229, 0.28);
    }


    div.stButton > button[kind="primary"]:hover {

        background: linear-gradient(
            135deg,
            #4338ca,
            #6d28d9
        );

        transform: translateY(-3px);

        box-shadow:
            0 14px 30px rgba(79, 70, 229, 0.36);
    }


    div.stButton > button[kind="primary"]:active {

        transform: translateY(0px);

        box-shadow:
            0 6px 15px rgba(79, 70, 229, 0.25);
    }


    /* =====================================================
       RESET BUTTON
       ===================================================== */

    div.stButton > button[kind="secondary"] {

        background: rgba(255, 255, 255, 0.88);

        color: #475569;

        border: 1px solid #cbd5e1;

        box-shadow:
            0 5px 15px rgba(15, 23, 42, 0.05);
    }


    div.stButton > button[kind="secondary"]:hover {

        background: #ffffff;

        color: #312e81;

        border-color: #818cf8;

        transform: translateY(-3px);

        box-shadow:
            0 10px 24px rgba(79, 70, 229, 0.14);
    }


    /* =====================================================
       BUTTON FOCUS
       ===================================================== */

    div.stButton > button:focus {

        outline: none !important;

        box-shadow:
            0 0 0 3px rgba(99, 102, 241, 0.18),
            0 8px 20px rgba(15, 23, 42, 0.10);
    }


    /* =====================================================
       RESULT HEADING
       ===================================================== */

    .result-heading {

        text-align: center;

        font-size: 29px;

        font-weight: 850;

        color: #312e81;

        margin-top: 10px;

        margin-bottom: 5px;
    }


    .result-subtitle {

        text-align: center;

        color: #64748b;

        font-size: 14px;

        margin-bottom: 18px;
    }


    /* =====================================================
       METRIC CARDS
       ===================================================== */

    div[data-testid="stMetric"] {

        background:
            rgba(255, 255, 255, 0.90);

        padding: 19px;

        border-radius: 17px;

        border: 1px solid #e2e8f0;

        box-shadow:
            0 7px 20px rgba(15, 23, 42, 0.06);

        min-height: 105px;

        transition: 0.2s ease;
    }


    div[data-testid="stMetric"]:hover {

        transform: translateY(-2px);

        box-shadow:
            0 10px 25px rgba(15, 23, 42, 0.09);
    }


    div[data-testid="stMetricLabel"] {

        color: #64748b;

        font-weight: 650;
    }


    div[data-testid="stMetricValue"] {

        color: #1e293b;

        font-weight: 800;
    }


    /* =====================================================
       SUCCESS MESSAGE
       ===================================================== */

    div[data-testid="stAlert"] {

        border-radius: 14px;
    }


    /* =====================================================
       EXPANDER
       ===================================================== */

    div[data-testid="stExpander"] {

        border-radius: 15px;

        border: 1px solid #e2e8f0;

        background:
            rgba(255, 255, 255, 0.72);

        box-shadow:
            0 5px 15px rgba(15, 23, 42, 0.04);
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer-line {

        border-top: 1px solid #cbd5e1;

        margin-top: 48px;

        padding-top: 20px;
    }


    .footer-title {

        text-align: center;

        color: #334155;

        font-size: 14px;

        font-weight: 750;
    }


    .footer-text {

        text-align: center;

        color: #94a3b8;

        font-size: 12px;

        margin-top: 5px;
    }


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 768px) {

        .main-title {
            font-size: 34px;
        }

        .main-subtitle {
            font-size: 15px;
        }

        .section-heading {
            font-size: 22px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD MODEL AND SCALER
# =========================================================

@st.cache_resource
def load_models():

    model = joblib.load(
        "models/linear_regression_model.pkl"
    )

    scaler = joblib.load(
        "models/standard_scaler.pkl"
    )

    return model, scaler


try:

    model, scaler = load_models()

except Exception as e:

    st.error("❌ Unable to load model files.")

    st.code(str(e))

    st.stop()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">'
    '🏡 House Price Predictor'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="main-subtitle">'
    'Predict the estimated market value of a house using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="status-box">'
    '🤖 Powered by Linear Regression • Scikit-learn'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# PROPERTY INFORMATION
# =========================================================

st.markdown(
    '<div class="section-heading">'
    '🏠 Property Information'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="section-text">'
    'Enter the characteristics of the house and surrounding area.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# INPUTS
# =========================================================

col1, col2 = st.columns(
    2,
    gap="large"
)


with col1:

    avg_income = st.number_input(
        "💰 Average Area Income",
        min_value=0.0,
        step=1000.0,
        key="avg_income"
    )


    house_age = st.number_input(
        "🏚️ Average Area House Age",
        min_value=0.0,
        step=0.1,
        key="house_age"
    )


    rooms = st.number_input(
        "🛋️ Average Area Number of Rooms",
        min_value=1.0,
        step=0.1,
        key="rooms"
    )


with col2:

    bedrooms = st.number_input(
        "🛏️ Average Area Number of Bedrooms",
        min_value=1.0,
        step=0.1,
        key="bedrooms"
    )


    population = st.number_input(
        "👥 Area Population",
        min_value=0.0,
        step=1000.0,
        key="population"
    )


# =========================================================
# ACTION BUTTONS
# =========================================================

st.write("")


button_left, button_center, button_right = st.columns(
    [1, 2.2, 1]
)


with button_center:

    predict_button = st.button(
        "🔮  Predict House Price",
        type="primary",
        use_container_width=True
    )


    st.write("")


    refresh_button = st.button(
        "↻  Reset Input Values",
        type="secondary",
        use_container_width=True,
        on_click=reset_values
    )


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    input_data = np.array(
        [[
            avg_income,
            house_age,
            rooms,
            bedrooms,
            population
        ]]
    )


    try:

        # =================================================
        # SCALE INPUT
        # =================================================

        input_scaled = scaler.transform(
            input_data
        )


        # =================================================
        # PREDICT
        # =================================================

        prediction = model.predict(
            input_scaled
        )


        predicted_price_usd = float(
            prediction[0]
        )


        # Prevent negative prediction

        predicted_price_usd = max(
            predicted_price_usd,
            0
        )


        # =================================================
        # USD TO INR
        # =================================================

        usd_to_inr = 88


        predicted_price_inr = (
            predicted_price_usd * usd_to_inr
        )


        # =================================================
        # SUCCESS MESSAGE
        # =================================================

        st.write("")


        st.success(
            "🎯 Prediction generated successfully!"
        )


        # =================================================
        # RESULT HEADING
        # =================================================

        st.markdown(
            '<div class="result-heading">'
            '💰 Estimated House Price'
            '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="result-subtitle">'
            'Estimated value based on the property characteristics'
            '</div>',
            unsafe_allow_html=True
        )


        # =================================================
        # PRICE CARDS
        # =================================================

        price_col1, price_col2 = st.columns(
            2,
            gap="large"
        )


        with price_col1:

            st.metric(
                label="🇺🇸 Estimated Price (USD)",
                value=f"$ {predicted_price_usd:,.2f}"
            )


        with price_col2:

            st.metric(
                label="🇮🇳 Estimated Price (INR)",
                value=f"₹ {predicted_price_inr:,.2f}"
            )


        st.caption(
            "💱 Conversion shown using an approximate rate "
            "of ₹88 per USD. The trained model prediction "
            "is in USD."
        )


        # =================================================
        # PROPERTY SUMMARY
        # =================================================

        st.write("")


        st.subheader(
            "📊 Property Summary"
        )


        summary1, summary2, summary3 = st.columns(
            3
        )


        with summary1:

            st.metric(
                "💰 Area Income",
                f"${avg_income:,.0f}"
            )


        with summary2:

            st.metric(
                "🏚️ House Age",
                f"{house_age:.1f} years"
            )


        with summary3:

            st.metric(
                "🛋️ Rooms",
                f"{rooms:.1f}"
            )


        summary4, summary5 = st.columns(
            2
        )


        with summary4:

            st.metric(
                "🛏️ Bedrooms",
                f"{bedrooms:.1f}"
            )


        with summary5:

            st.metric(
                "👥 Population",
                f"{population:,.0f}"
            )


        # =================================================
        # HOW IT WORKS
        # =================================================

        st.write("")


        with st.expander(
            "ℹ️ How does this prediction work?"
        ):

            st.write(
                """
                This application uses a trained **Linear Regression**
                machine learning model to estimate house prices.

                **Features used by the model:**

                • Average Area Income  
                • Average Area House Age  
                • Average Area Number of Rooms  
                • Average Area Number of Bedrooms  
                • Area Population  

                The entered values are first transformed using the
                saved **StandardScaler** and then passed to the
                trained Linear Regression model.
                """
            )


    except Exception as e:

        st.error(
            "❌ Prediction failed."
        )

        st.code(str(e))


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer-line"></div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="footer-title">'
    '🏡 House Price Prediction'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="footer-text">'
    'Python • NumPy • Scikit-learn • Streamlit'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="footer-text">'
    'Machine Learning Based House Price Estimation'
    '</div>',
    unsafe_allow_html=True
)