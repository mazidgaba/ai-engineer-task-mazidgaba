"""
ADGM Corporate Agent - Main Application
Comprehensive ADGM compliance analysis and document processing
"""

import gradio as gr
import json
import logging
from typing import List, Dict, Any
from pathlib import Path
from doc_processing import DocumentProcessor
from checklist import get_all_processes, get_checklist_for_process

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ADGMCorporateAgent:
    def __init__(self):
        self.processor = DocumentProcessor()
        self.processed_documents = []
        logger.info("ADGM Corporate Agent initialized")

    def process_documents(self, files, process_type: str) -> tuple:
        """
        Main function to process uploaded documents for ADGM compliance
        """
        if not files:
            return (
                "No files uploaded",
                "No files to process",
                "Please upload documents for analysis"
            )
        
        if not process_type:
            return (
                "No process type selected",
                "No process specified",
                "Please select a business process"
            )

        try:
            # Process each document
            documents_analysis = []
            reviewed_files = []
            
            for file in files:
                # Get file path
                if hasattr(file, 'name'):
                    file_path = file.name
                else:
                    file_path = str(file)
                
                logger.info(f"Processing file: {file_path}")
                
                # Parse document
                content, metadata = self.processor.parse_docx(file_path)
                
                # Detect document type
                doc_type, category, confidence = self.processor.detect_document_type(content, Path(file_path).name)
                
                # Check ADGM compliance
                issues = self.processor.check_adgm_compliance(content, doc_type)
                
                # Create document analysis record
                doc_analysis = {
                    "filename": Path(file_path).name,
                    "full_path": file_path,
                    "document_type": doc_type,
                    "category": category,
                    "confidence_score": confidence,
                    "metadata": metadata,
                    "issues": issues,
                    "issue_count": len(issues),
                    "high_severity_issues": len([i for i in issues if i.get("severity") == "High"])
                }
                
                documents_analysis.append(doc_analysis)
                
                # Generate reviewed document with comments if there are issues
                if issues:
                    try:
                        reviewed_file_path = self.processor.insert_comments(file_path, issues)
                        reviewed_files.append(reviewed_file_path)
                        logger.info(f"Generated reviewed document: {reviewed_file_path}")
                    except Exception as e:
                        logger.error(f"Error generating reviewed document: {str(e)}")
            
            # Generate comprehensive report
            comprehensive_report = self.processor.generate_comprehensive_report(
                documents_analysis, 
                process_type
            )
            
            # Generate status message
            status_message = self._generate_status_message(comprehensive_report)
            
            # Return results
            return (
                json.dumps(comprehensive_report, indent=2),
                "\n".join(reviewed_files) if reviewed_files else "No reviewed documents generated",
                status_message
            )
            
        except Exception as e:
            logger.error(f"Error processing documents: {str(e)}")
            return (
                f"Error: {str(e)}",
                "Processing failed",
                f"❌ Error occurred: {str(e)}"
            )

    def _generate_status_message(self, report: Dict) -> str:
        """Generate human-readable status message"""
        try:
            if report.get("status") == "error":
                return f"❌ {report.get('message', 'Unknown error')}"
            
            compliance_status = report.get("compliance_status", "Unknown")
            checklist = report.get("checklist_verification", {})
            total_issues = report.get("total_issues_found", 0)
            high_issues = report.get("high_severity_issues", 0)
            
            status_parts = []
            
            # Compliance status
            if compliance_status == "Fully Compliant":
                status_parts.append("✅ Fully Compliant")
            elif compliance_status == "Partially Compliant":
                status_parts.append("⚠️ Partially Compliant")
            else:
                status_parts.append("❌ Non-Compliant")
            
            # Checklist status
            if checklist:
                completeness = checklist.get("completeness_percentage", 0)
                missing_count = checklist.get("missing_count", 0)
                
                if missing_count == 0:
                    status_parts.append("📋 All required documents present")
                else:
                    status_parts.append(f"📋 Missing {missing_count} required documents")
                
                status_parts.append(f"📊 Document completeness: {completeness}%")
            
            # Issues summary
            if total_issues == 0:
                status_parts.append("✅ No compliance issues found")
            else:
                status_parts.append(f"⚠️ Found {total_issues} compliance issues")
                if high_issues > 0:
                    status_parts.append(f"🚨 {high_issues} high severity issues")
            
            return "\n".join(status_parts)
            
        except Exception as e:
            logger.error(f"Error generating status message: {str(e)}")
            return "Error generating status message"

    def get_process_info(self, process_name: str) -> str:
        """Get information about a specific business process"""
        try:
            checklist = get_checklist_for_process(process_name)
            if not checklist:
                return f"Unknown process: {process_name}"
            
            info = f"**{process_name}**\n\n"
            info += f"**Description:** {checklist['description']}\n"
            info += f"**Priority:** {checklist['priority']}\n\n"
            info += "**Required Documents:**\n"
            
            for i, doc in enumerate(checklist['required_documents'], 1):
                info += f"{i}. {doc}\n"
            
            return info
            
        except Exception as e:
            logger.error(f"Error getting process info: {str(e)}")
            return f"Error retrieving process information: {str(e)}"

def main():
    """Main application entry point"""
    agent = ADGMCorporateAgent()
    
    # Get available processes
    available_processes = get_all_processes()
    
    # Create Gradio interface
    with gr.Blocks(title="ADGM Corporate Agent - Professional Edition", theme=gr.themes.Soft()) as iface:
        gr.Markdown("""
        # 🏛️ ADGM Corporate Agent - Professional Edition
        
        **Comprehensive ADGM Compliance Analysis & Document Processing**
        
        This professional-grade tool provides:
        - 📋 **Document Checklist Verification** against ADGM requirements
        - 🔍 **Advanced Document Type Detection** with confidence scoring
        - ⚖️ **Comprehensive Compliance Checking** for ADGM regulations
        - 📝 **Inline Document Comments** for identified issues
        - 📊 **Detailed Compliance Reports** with actionable recommendations
        """)
        
        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown("### 📤 Document Upload")
                file_input = gr.File(
                    label="Upload Documents (.docx)",
                    file_count="multiple"
                )
                
                gr.Markdown("### 🎯 Business Process Selection")
                process_dropdown = gr.Dropdown(
                    choices=available_processes,
                    label="Select Business Process",
                    info="Choose the business process these documents are for"
                )
                
                process_info_btn = gr.Button("ℹ️ Get Process Information")
                process_info_output = gr.Markdown(label="Process Information")
                
                process_btn = gr.Button("🚀 Process Documents", variant="primary")
            
            with gr.Column(scale=3):
                gr.Markdown("### 📊 Analysis Results")
                
                with gr.Tab("📋 Comprehensive Report"):
                    report_output = gr.Textbox(label="Compliance Report", lines=15)
                
                with gr.Tab("📝 Reviewed Documents"):
                    reviewed_files_output = gr.Textbox(
                        label="Reviewed Documents", 
                        lines=5,
                        info="Paths to documents with inline compliance comments"
                    )
                
                with gr.Tab("📈 Status Summary"):
                    status_output = gr.Textbox(
                        label="Compliance Status", 
                        lines=10,
                        info="Human-readable compliance summary"
                    )
        
        # Event handlers
        process_info_btn.click(
            fn=agent.get_process_info,
            inputs=[process_dropdown],
            outputs=[process_info_output]
        )
        
        process_btn.click(
            fn=agent.process_documents,
            inputs=[file_input, process_dropdown],
            outputs=[report_output, reviewed_files_output, status_output]
        )
        
        gr.Markdown("""
        ---
        
        ### 🔧 How It Works
        
        1. **Upload Documents**: Select your .docx files for analysis
        2. **Choose Process**: Select the business process (e.g., Company Incorporation)
        3. **Process**: Click "Process Documents" to analyze compliance
        4. **Review Results**: Check the comprehensive report and status
        5. **Download Reviewed Documents**: Get documents with inline compliance comments
        
        ### 📚 Supported Document Types
        
        - Articles of Association
        - Memorandum of Association
        - UBO Declarations
        - Board Resolutions
        - Employment Contracts
        - Compliance Manuals
        - And more...
        
        ### ⚖️ Compliance Checks
        
        - **Jurisdiction**: Ensures ADGM Courts are specified
        - **Governing Law**: Verifies ADGM/English Law compliance
        - **Document Structure**: Checks for proper formatting
        - **Content Requirements**: Validates document-specific requirements
        - **Signature Blocks**: Ensures proper execution
        """)
    
    # Launch the application
    iface.launch(
        server_port=7862,
        inbrowser=True
    )

if __name__ == "__main__":
    print("🚀 Starting ADGM Corporate Agent - Professional Edition...")
    print("📱 The app will open in your browser at http://127.0.0.1:7862")
    main() 