import streamlit as st
import pandas as pd

# Streamlit app
def main():
    st.title("Excel Data Analyzer")
    st.write("Upload an Excel file to visualize and analyze its contents.")

    # File uploader
    uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
    if uploaded_file is not None:
        # Read Excel file
        try:
            # Load the Excel file into a Pandas DataFrame
            excel_data = pd.ExcelFile(uploaded_file)
            st.write("Available Sheets:", excel_data.sheet_names)

            # Sheet selection
            sheet = st.selectbox("Select a sheet to display", excel_data.sheet_names)
            data = excel_data.parse(sheet)

            # Display the data
            st.subheader(f"Data from {sheet}")
            st.dataframe(data)

            # Show basic stats
            st.subheader("Data Summary")
            st.write(data.describe())

            # Visualization options
            st.subheader("Visualizations")
            if st.checkbox("Show Line Chart"):
                st.line_chart(data.select_dtypes(include=["number"]))

            if st.checkbox("Show Bar Chart"):
                st.bar_chart(data.select_dtypes(include=["number"]))

            if st.checkbox("Show Column Selector for Custom Chart"):
                columns = st.multiselect("Select columns to visualize", data.columns)
                if len(columns) > 0:
                    st.line_chart(data[columns])

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
