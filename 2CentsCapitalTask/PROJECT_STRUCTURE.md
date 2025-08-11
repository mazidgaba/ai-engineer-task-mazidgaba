# 📁 ADGM Corporate Agent - Project Structure

## 🏗️ **Organized Project Layout**

```
2cents/
├── 📁 src/                           # Source code package
│   ├── __init__.py                   # Package initialization
│   ├── adgm_corporate_agent.py      # Main application
│   ├── doc_processing.py            # Document processing core
│   └── checklist.py                 # ADGM compliance checklists
│
├── 📁 tests/                         # Testing and validation
│   └── test_functionality.py        # Core functionality tests
│
├── 📁 samples/                       # Sample documents and generators
│   ├── sample_document.py           # Document generation script
│   └── docs/                        # Sample documents
│       ├── Sample_Articles_of_Association.docx
│       └── Sample_UBO_Declaration.docx
│
├── 📁 assets/                        # Reference materials and resources
│   ├── Data Sources.docx            # ADGM reference document
│   ├── Data Sources.pdf             # ADGM reference PDF
│   └── Task.pdf                     # Project requirements
│
├── 📁 .venv/                         # Python virtual environment
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation
├── main.py                          # Main entry point
└── PROJECT_STRUCTURE.md             # This file
```

## 🎯 **Directory Purposes**

### **`src/` - Source Code**
- **`adgm_corporate_agent.py`**: Main Gradio application
- **`doc_processing.py`**: Core document analysis and processing
- **`checklist.py`**: ADGM compliance checklists and verification
- **`__init__.py`**: Package initialization and exports

### **`tests/` - Testing**
- **`test_functionality.py`**: Unit tests for core functions
- **Purpose**: Validate functionality without launching UI

### **`samples/` - Sample Materials**
- **`sample_document.py`**: Script to generate test documents
- **`docs/`**: Sample .docx files for testing
- **Purpose**: Provide test data and examples

### **`assets/` - Reference Materials**
- **Data Sources**: ADGM reference documents
- **Task.pdf**: Project requirements and specifications
- **Purpose**: Store reference materials and requirements

## 🚀 **How to Run**

### **Option 1: From Root Directory (Recommended)**
```bash
python main.py
```

### **Option 2: From Source Directory**
```bash
cd src
python adgm_corporate_agent.py
```

### **Option 3: Run Tests**
```bash
cd tests
python test_functionality.py
```

### **Option 4: Generate Sample Documents**
```bash
cd samples
python sample_document.py
```

## 🔧 **Development Workflow**

1. **Source Code**: Edit files in `src/` directory
2. **Testing**: Add tests in `tests/` directory
3. **Samples**: Update sample documents in `samples/` directory
4. **Documentation**: Update README.md and PROJECT_STRUCTURE.md
5. **Dependencies**: Update requirements.txt as needed

## 📋 **Benefits of This Structure**

✅ **Professional Organization**: Follows Python best practices
✅ **Clear Separation**: Source, tests, samples, and assets are separate
✅ **Easy Navigation**: Developers can quickly find what they need
✅ **Scalable**: Easy to add new modules and features
✅ **Maintainable**: Clear structure makes maintenance easier
✅ **Import-Friendly**: Proper package structure for imports
✅ **Testing Ready**: Dedicated testing directory
✅ **Documentation**: Clear project structure documentation

## 🎉 **Ready for Production**

This organized structure makes the ADGM Corporate Agent ready for:
- Professional development
- Team collaboration
- Easy deployment
- Future enhancements
- Proper testing
- Documentation maintenance
