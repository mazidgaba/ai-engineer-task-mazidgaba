"""
ADGM Corporate Agent - Professional Edition
A comprehensive AI-powered legal assistant for ADGM compliance analysis

This package provides:
- Document processing and analysis
- ADGM compliance checking
- Checklist verification
- Inline commenting and review
"""

__version__ = "1.0.0"
__author__ = "ADGM Corporate Agent Team"
__description__ = "AI-powered legal assistant for ADGM compliance"

from .adgm_corporate_agent import ADGMCorporateAgent
from .doc_processing import DocumentProcessor
from .checklist import get_all_processes, get_checklist_for_process

__all__ = [
    "ADGMCorporateAgent",
    "DocumentProcessor", 
    "get_all_processes",
    "get_checklist_for_process"
]
