import streamlit as st
import pandas as pd
import requests
import tempfile

API_URL = "http://localhost:8000/classify/"

st.set_page_config(page_title="Log Classifier", layout="centered")
st.title("📄 Log Classification Frontend")

st.markdown("""
Upload a log CSV with `source` and `log_message` columns.  
The backend will return the classified logs.
""")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    try:
        with st.spinner("Uploading and classifying logs..."):
            files = {"file": (uploaded_file.name, uploaded_file, "text/csv")}
            response = requests.post(API_URL, files=files)

        if response.status_code != 200:
            st.error(f"❌ Server returned error: {response.json()['detail']}")
        else:
            # Save response CSV to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
                tmp.write(response.content)
                tmp_path = tmp.name

            # Read and display DataFrame
            df = pd.read_csv(tmp_path)
            st.success("✅ Logs classified successfully!")
            st.subheader("🔍 Preview of Results")
            st.dataframe(df.head(), use_container_width=True)

            # Download button
            with open(tmp_path, "rb") as f:
                st.download_button(
                    label="📥 Download Classified CSV",
                    data=f,
                    file_name="classified_logs.csv",
                    mime="text/csv"
                )

            # Link to open file directly (useful in local apps)
            st.markdown(f'<a href="file://{tmp_path}" target="_blank">📂 Open CSV File</a>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
