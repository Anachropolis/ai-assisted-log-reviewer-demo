import streamlit as st
from ingest_module.document_loader import DocumentLoader
from ui_features.ui_features import InterfaceFeatures


loader = DocumentLoader()


sidebar = InterfaceFeatures()
sidebar.create_button("Home")
clicked = sidebar.get_clicked()

if clicked:
    st.switch_page("streamlit_app_homepage.py")



log_id = st.session_state.get("log_id", "N/A")
log_review = st.session_state.get("generated_review", None)

if log_review is None:
    st.warning("No review has been generated yet. Return to the homepage and run a log review.")
    st.stop()

for key, value in log_review.items():
    """Generate report in markdown from retrieved json"""

    st.markdown(f"## {key.replace('_', ' ').title()}", unsafe_allow_html=True)
    if type(value) is list:
        for item in value:

            if key == "relevant_references":
                for ref in value:
                    with st.expander(ref.get("title", "Reference")):
                        st.write(f"**Source:** {ref.get('source_file', 'Unknown')}")
                        st.write(ref.get("why_relevant", ""))

            else:
                st.markdown(f"- {item}", unsafe_allow_html=True)
    else:
        st.markdown(value, unsafe_allow_html=True)


