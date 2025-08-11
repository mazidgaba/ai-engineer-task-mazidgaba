"""
ADGM Document Checklists
Based on Data Sources.pdf and ADGM requirements
"""

ADGM_CHECKLISTS = {
    "Company Incorporation": {
        "required_documents": [
            "Articles of Association",
            "Memorandum of Association", 
            "Board Resolution Template",
            "Shareholder Resolution Template",
            "UBO Declaration Form",
            "Register of Members and Directors",
            "Incorporation Application Form",
            "Change of Registered Address Notice"
        ],
        "description": "Complete set of documents required for company formation in ADGM",
        "priority": "High"
    },
    "Licensing": {
        "required_documents": [
            "Licensing Application Form",
            "Business Plan Template",
            "Financial Projections",
            "Risk Assessment Document",
            "Compliance Manual",
            "Anti-Money Laundering Policy",
            "Risk Management Policy"
        ],
        "description": "Documents needed for obtaining ADGM business license",
        "priority": "High"
    },
    "Employment": {
        "required_documents": [
            "Standard Employment Contract Template",
            "Confidentiality Agreement",
            "Non-Compete Agreement",
            "Employee Handbook",
            "HR Policies and Procedures"
        ],
        "description": "Employment-related documents for ADGM companies",
        "priority": "Medium"
    },
    "Compliance": {
        "required_documents": [
            "Compliance Manual",
            "Risk Management Policy",
            "Anti-Money Laundering Policy",
            "Data Protection Policy",
            "Annual Compliance Report Template"
        ],
        "description": "Ongoing compliance documentation requirements",
        "priority": "High"
    },
    "Corporate Governance": {
        "required_documents": [
            "Board Charter",
            "Corporate Governance Manual",
            "Code of Conduct",
            "Whistleblower Policy",
            "Board Meeting Minutes Template"
        ],
        "description": "Corporate governance framework documents",
        "priority": "Medium"
    }
}

def get_checklist_for_process(process_name: str) -> dict:
    """Get checklist for a specific business process"""
    return ADGM_CHECKLISTS.get(process_name, {})

def get_all_processes() -> list:
    """Get list of all available business processes"""
    return list(ADGM_CHECKLISTS.keys())

def verify_checklist_completeness(uploaded_docs: list, process_name: str) -> dict:
    """Verify if all required documents are present for a process"""
    checklist = get_checklist_for_process(process_name)
    if not checklist:
        return {
            "status": "error",
            "message": f"Unknown process: {process_name}"
        }
    
    required_docs = checklist["required_documents"]
    uploaded_doc_names = [doc.lower() for doc in uploaded_docs]
    
    missing_docs = []
    present_docs = []
    
    for req_doc in required_docs:
        if any(req_doc.lower() in uploaded for uploaded in uploaded_doc_names):
            present_docs.append(req_doc)
        else:
            missing_docs.append(req_doc)
    
    completeness_percentage = (len(present_docs) / len(required_docs)) * 100
    
    return {
        "process": process_name,
        "required_count": len(required_docs),
        "uploaded_count": len(present_docs),
        "missing_count": len(missing_docs),
        "completeness_percentage": round(completeness_percentage, 2),
        "present_documents": present_docs,
        "missing_documents": missing_docs,
        "status": "complete" if missing_docs == [] else "incomplete"
    } 