# Disney Reviews Analyzer

## Description
A system for analyzing Disney parks reviews, enabling data visualization, graph generation, and report export in multiple formats.

## Features

### 1. Data Visualization
- [x] List reviews by park
- [x] Count reviews by park and location
- [x] Annual rating average by park
- [x] Average by park and location (table)

### 2. Graphs
- [x] Reviews distribution by park (pie)
- [x] Average ratings by park (bar)
- [x] Top 10 locations by park (bar)
- [x] Monthly average by park (bar)

### 3. Export
- [x] TXT Format (structured text)
- [x] CSV Format (spreadsheet)
- [x] JSON Format (structured data)

## Project Structure
```
project/
├── data/
│   └── disneyland_reviews.csv    # Dataset
├── tests/
│   └── test_process.py           # Unit tests
├── main.py                       # Entry point
├── process.py                    # Data processing
├── tui.py                        # Text interface
├── visual.py                     # Graph generation
└── exporter.py                   # Data export
```

## Requirements
- Python 3.7+
- matplotlib==3.7.1 (for graphs)
- pytest==7.3.1 (for tests)

## How to Run

1. **Setup**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install matplotlib==3.7.1 pytest==7.3.1
```

2. **Execution**
```bash
python main.py
```

3. **Testing**
```bash
python -m pytest tests/
```

## Implemented Features

### User Interface
- [x] Interactive main menu
- [x] Submenus for each functionality
- [x] Input validation
- [x] Error handling

### Data Processing
- [x] Efficient CSV loading
- [x] Statistical calculations
- [x] Filters and aggregations
- [x] Automatic date conversion

### Visualization
- [x] Interactive graphs
- [x] Multiple visualization types
- [x] Proper formatting
- [x] Clear titles and legends

### Export
- [x] Multiple supported formats
- [x] Structured data
- [x] UTF-8 encoding
- [x] Error handling

## Tests
- [x] Unit tests for critical functions
- [x] Data loading verification
- [x] Statistical calculations validation
- [x] Summary functions testing

## Code Standards
- [x] Complete documentation (docstrings)
- [x] Static typing
- [x] PEP 8 compliance
- [x] Modular organization

## Error Handling
- [x] User input validation
- [x] KeyboardInterrupt handling
- [x] Clear error messages
- [x] Invalid state recovery

## Notes
- Simple and intuitive text interface
- Clear separation of module responsibilities
- Well-documented and tested code
- Easy extensibility for new export formats

## Special Features
- Use of dataclasses for data structuring
- Strategy pattern for export
- Detailed statistical analysis
- Custom visualizations

## Project Status
- [x] MVP Complete
- [x] Tests Implemented
- [x] Documentation Completed
- [x] Ready for Use

## Known Issues
- If experiencing graph issues on Windows, ensure matplotlib is correctly installed with the specified version
- On some systems, graph windows may need to be manually closed to continue using the program
