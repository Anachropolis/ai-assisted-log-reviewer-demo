from api_module.api_client import ApiClient
from ingest_module.vector_store import VectorStore
from review_module.reviewer import LogReviewer
from review_module.llm_client import LLMClient
from ui_features.ui_features import InterfaceFeatures
import streamlit as st



endpoint = "operator-logs"
client = ApiClient()
llm_client = LLMClient()
log_list = client.fetch_log_list(endpoint)
log_ids = [log["log_id"] for log in log_list]
sidebar = InterfaceFeatures()



st.markdown("<h1 style='text-align: center;'>Log List</h1>", unsafe_allow_html=True)


for entry in log_list:

    with st.expander(f"{entry['log_id']} — {entry['event_type']}"):
        st.write(f"**Timestamp:** {entry['timestamp']}")
        st.write(f"**Facility:** {entry['facility']}")
        st.write(f"**Severity:** {entry['severity']}")
        st.write(entry["log_text"])

sidebar.create_dropdown("Log Select", log_ids)
sidebar.create_button("Review")

selection = sidebar.get_selection()
clicked = sidebar.get_clicked()

if clicked:
    st.session_state["log_id"] = selection
    selected_log = client.fetch_operator_log(endpoint, selection)
    relevant_references = VectorStore().retrieve_relevant_references(selected_log["log_text"])
    with st.sidebar:
        with st.spinner("Analyzing log entry...", show_time=True):
            st.session_state["generated_review"] = LogReviewer(llm_client).review_log_entry(selected_log, relevant_references)

            st.switch_page("pages/streamlit_report.py")

