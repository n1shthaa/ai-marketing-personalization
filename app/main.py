import streamlit as st
from layout import show_homepage          # ⬅️ Remove "app."
from utils import connect_db 

st.set_page_config(page_title="AI Marketing Personalization", layout="wide")

# Title Bar
st.title("📈 AI Marketing Campaign Personalization Dashboard")

# Navigation
page = st.sidebar.selectbox("Choose a Page", ["Home", "Customer Segments", "Offer Recommendations", "Predictive Analysis", "Message Generator"])

# DB Connection (Lazy loading)
conn = connect_db()
if conn:
    st.success("✅ Connected to SQLite database.")
    # Optional test query
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    st.write("Tables:", tables)
else:
    st.error("❌ Could not connect to SQLite DB.")
# Page Routing
if page == "Home":
    show_homepage()
elif page == "Customer Segments":
    st.write("🧠 Customer segmentation visualization will go here.")
elif page == "Offer Recommendations":
    st.write("🎁 Recommended offers for each user segment will go here.")
elif page == "Predictive Analysis":
    st.write("📊 Predict response probabilities to offers here.")
elif page == "Message Generator":
    st.write("💬 NLP-based personalized messaging area.")
import streamlit as st
from layout import show_homepage
from utils import connect_db, fetch_customers, fetch_offers

# Streamlit page config
st.set_page_config(page_title="AI Marketing Personalization", layout="wide")

# Title bar
st.title("📈 AI Marketing Campaign Personalization Dashboard")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Choose a Page",
    [
        "Home",
        "View Customers",
        "View Offers",
        "Customer Segments",
        "Offer Recommendations",
        "Predictive Analysis",
        "Message Generator"
    ]
)

# Connect to SQLite database
conn = connect_db()
if conn:
    st.success("✅ Connected to SQLite database.")
else:
    st.error("❌ Could not connect to SQLite database.")
    st.stop()

# Page Routing
if page == "Home":
    show_homepage()

elif page == "View Customers":
    st.subheader("👥 Customer List")
    df_customers = fetch_customers(conn)
    st.dataframe(df_customers, use_container_width=True)

elif page == "View Offers":
    st.subheader("🎁 Available Offers")
    df_offers = fetch_offers(conn)
    st.dataframe(df_offers, use_container_width=True)

elif page == "Customer Segments":
    st.write("🧠 Customer segmentation visualization will go here.")

elif page == "Offer Recommendations":
    st.write("🎯 Personalized offers will be displayed here.")

elif page == "Predictive Analysis":
    st.write("📊 Predict response probabilities to offers here.")

elif page == "Message Generator":
    st.write("💬 NLP-based personalized message generator will go here.")
