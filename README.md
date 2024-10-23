# CSV to SQL Converter

A streamlined web application built with Streamlit that converts CSV files into SQL statements. This tool automatically detects column data types and generates both CREATE TABLE and INSERT statements for your data.

![CSV to SQL Converter](https://placeholder.com/readme-header)

## Features

- 🔄 Convert CSV files to SQL statements
- 🔍 Automatic data type detection (INTEGER, REAL, TEXT)
- 📊 Support for large CSV files (up to 200MB)
- 📝 Generate CREATE TABLE statements
- ➕ Generate INSERT statements
- 👀 Preview generated SQL
- ⬇️ Download SQL file option
- 🎨 Modern, responsive UI design

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/csv-to-sql-converter.git
cd csv-to-sql-converter
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install streamlit
```

4. Create the project structure:
```
csv-to-sql-converter/
├── app.py
├── styles.css
├── .streamlit/
│   └── config.toml
└── README.md
```

## File Structure

### `app.py`
The main application file containing the Streamlit web application logic. Key components include:
- File upload handling
- CSV parsing
- Data type inference
- SQL statement generation
- User interface layout

### `styles.css`
Custom styling for the application, including:
- Color scheme
- Button styling
- Input field formatting
- Layout adjustments
- Responsive design elements

### `.streamlit/config.toml`
Configuration file for Streamlit theme settings:
- Color scheme definitions
- Font settings
- Background colors
- Text colors

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Access the web interface at `http://localhost:8501`

3. Using the converter:
   - Upload a CSV file using the sidebar
   - Enter a name for your SQL table
   - Click "Generate SQL"
   - Preview the generated SQL
   - Download the SQL file

## Features in Detail

### Automatic Data Type Detection
The application automatically infers SQL data types based on column contents:
- `INTEGER`: For whole numbers
- `REAL`: For decimal numbers
- `TEXT`: For text and mixed content

### SQL Generation
Generates two types of SQL statements:
1. CREATE TABLE statement with appropriate column definitions
2. INSERT statements containing all data from the CSV

### User Interface
- Clean, modern design
- Intuitive layout
- Responsive components
- Clear visual hierarchy
- Informative messages and tooltips

## Customization

### Modifying the Theme
Edit `.streamlit/config.toml` to change the application theme:
```toml
[theme]
primaryColor = "#FF6F61"            # Primary UI elements
backgroundColor = "#F0F4F8"         # Main background
secondaryBackgroundColor = "#FFFFFF" # Secondary elements
textColor = "#333333"               # Text color
font = "sans serif"                 # Font family
base = "light"                      # Base theme
headerColor = "#FF6F61"             # Header color
```

### Customizing Styles
Edit `styles.css` to modify the application's appearance:
- Button styles
- Input field formatting
- Layout adjustments
- Custom components

## Technical Details

### Data Processing Flow
1. CSV file upload and validation
2. Header and data extraction
3. Data type inference for each column
4. SQL statement generation
5. Preview generation
6. File download preparation

### Performance Considerations
- Handles files up to 200MB
- Streaming data processing
- Efficient memory usage
- Optimized SQL generation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact [your contact information].

## Acknowledgments

- Streamlit team for the fantastic framework
- Contributors and users of the application

## Future Enhancements

Planned features for future releases:
- Support for additional SQL dialects
- Custom data type mapping
- Batch processing capabilities
- Schema validation options
- Advanced data transformation options

---
