import streamlit as st
import csv
import io
import time

def infer_data_type(value):
    if value.isdigit():
        return 'INTEGER'
    try:
        float(value)
        return 'REAL'
    except ValueError:
        return 'TEXT'

def read_file(file, table_name):
    content = file.getvalue().decode("utf-8")
    values = list(csv.reader(io.StringIO(content)))

    headers = values[0]
    data_types = [None] * len(headers)

    for row in values[1:]:
        for index, value in enumerate(row):
            inferred_type = infer_data_type(value)
            if data_types[index] is None:
                data_types[index] = inferred_type
            elif data_types[index] != inferred_type:
                data_types[index] = 'TEXT'

    column_definitions = [f"{header} {sql_type}" for header, sql_type in zip(headers, data_types)]
    create_table_sql = f"CREATE TABLE {table_name} (\n  {',\n  '.join(column_definitions)}\n);\n\n"

    sql_insert = f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES \n'
    
    for row in values[1:]:
        if not row:
            continue
        sql_values = []
        for index, value in enumerate(row):
            inferred_type = data_types[index]
            if inferred_type == 'INTEGER':
                sql_values.append(value)
            elif inferred_type == 'REAL':
                sql_values.append(value)
            else:
                sql_values.append(f"'{value}'")
        if sql_values:
            sql_insert += f"({', '.join(map(str, sql_values))}),\n"

    sql_insert = sql_insert.strip()[:-1] + ";\n"
    return create_table_sql + sql_insert

def main():
    st.set_page_config(page_title="CSV to SQL Converter", layout="wide")
    
    # Load custom CSS
    with open("styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    st.title("CSV to SQL Converter")
    
    # Add information text
    st.markdown("""
    <div class="info-text">
        <p><strong>How to use this converter:</strong></p>
        <ol>
            <li>Upload your CSV file using the sidebar (max 200MB)</li>
            <li>Enter a name for your SQL table</li>
            <li>Click 'Generate SQL' to create your SQL statements</li>
            <li>Preview the generated SQL and download the file</li>
        </ol>
        <p><em>The converter will automatically detect column types (INTEGER, REAL, or TEXT) based on your data.</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for file upload
    st.sidebar.header("Upload")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    
    # Main input for table name with custom styling
    st.markdown('<p class="upload-text">Enter the name of the table:</p>', unsafe_allow_html=True)
    table_name = st.text_input("", key="table_name", help="Enter the name for your SQL table")
    
    if st.button("Generate SQL"):
        if uploaded_file and table_name:
            with st.spinner("Generating SQL..."):
                time.sleep(1)  # Simulating delay
                output_sql = read_file(uploaded_file, table_name)
            output_sql_lines = output_sql.splitlines()
            preview_lines = output_sql_lines[:100]
            with st.expander("View Generated SQL", expanded=False):
                st.code("\n".join(preview_lines) + "\n... [and more]")
            output_file = io.BytesIO()
            output_file.write(output_sql.encode('utf-8'))
            output_file.seek(0)
            st.download_button("Download SQL file", output_file, file_name=f"{table_name}.sql", mime="text/plain")
        else:
            st.error("Please upload a CSV file and enter a table name.")

if __name__ == "__main__":
    main()