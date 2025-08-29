import streamlit as st
import pandas as pd

# Load Data
@st.cache_data
def load_data():
    students_df = pd.read_csv("student_details.csv")
    preferences_df = pd.read_csv("preference_data.csv")
    institutions_df = pd.read_csv("institution_data.csv")
    allocation_df = pd.read_csv("allocation_results.csv")
    return students_df, preferences_df, institutions_df, allocation_df

students_df, preferences_df, institutions_df, allocation_df = load_data()

# Streamlit Page Setup
st.set_page_config(page_title="Student College Allocation System", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>
        🎓 Student College Allocation System
    </h1>
    <p style='text-align: center;'>Enter your <b>UniqueID</b> to check your allocation details.</p>
    """,
    unsafe_allow_html=True
)

# Input box
unique_id = st.text_input("🔑 Enter Your UniqueID:", max_chars=10)

if unique_id:
    try:
        student_result = allocation_df[allocation_df['UniqueID'] == int(unique_id)]
    except:
        student_result = allocation_df[allocation_df['UniqueID'] == unique_id]

    if not student_result.empty:
        result = student_result.iloc[0]
        st.subheader("✅ Your Allocation Result")

        # Result card
        st.markdown(
            f"""
            <div style='background-color:#f0f8ff; padding:20px; border-radius:15px;'>
                <h3>👤 {result['Name']} ({result['UniqueID']})</h3>
                <p><b>Gender:</b> {result['Gender']}</p>
                <p><b>Caste:</b> {result['Caste']}</p>
                <p><b>Rank:</b> {result['Rank']}</p>
                <hr>
                <h4>🏫 College Allocation</h4>
                <p><b>College ID:</b> {result['CollegeID']}</p>
                <p><b>Institution:</b> {result['Institution']}</p>
                <p><b>Preference Number Used:</b> {result['PrefNumber'] if result['PrefNumber'] else 'N/A'}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("❌ Invalid ID. Please check and try again.")
else:
    st.info("ℹ️ Please enter your UniqueID to view your result.")

# Footer
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
