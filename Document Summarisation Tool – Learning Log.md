SEQATO LLM Awareness and Portfolio Development Program - Learning Log

Introduction

This document captures the detailed learning log and technical experiences during the SEQATO LLM Awareness and Portfolio Development Program – Phase 1: Document Summarisation Tool Project. It focuses on building a working pipeline to summarise documents (PDFs) using LLMs with LangChain, PyPDF, and Streamlit. This log documents the setup, development, troubleshooting, and successful implementation of the tool for internal and client-facing summarisation use cases.

Phase 1: Project 2 – Document Summarisation Tool (LLM + LangChain)

Setup and Tools

Installed Python, LangChain, PyPDF, Streamlit, ChromaDB, OpenAI/Groq SDKs.

Created a structured project folder:

summariser.py (core logic)

app.py (optional Streamlit UI)

requirements.txt

Prepared test PDFs (HR policies, marketing decks) for summarisation workflow validation.

Document Loading and Chunking

Utilised PyPDFLoader from LangChain to extract and clean text from PDFs.

Encountered issues with repetitive headers and footers in extracted text.

Implemented post-processing regex cleaning to remove unwanted repetitive lines, improving text clarity before summarisation.

LLM Summarisation Integration

Integrated OpenAI GPT-4o API for initial summarisation tests.

Faced token limit issues when sending large document chunks for summarisation.

Resolved by:

Splitting content into manageable chunks with slight sentence overlaps to preserve context.

Summarising each chunk separately, followed by a merged summary generation step for the final output.

Testing with Sample Documents

Uploaded HR policy documents and marketing decks for summarisation tests.

Identified issues with context fragmentation when chunking mid-topic.

Adjusted the chunking strategy by:

Overlapping sentences between chunks.

Experimenting with different chunk sizes (1000-1500 tokens) for optimal summarisation accuracy.

Handling Scanned PDFs

Tested scanned PDFs and found incomplete extraction due to lack of OCR.

Planned Tesseract OCR integration for scanned PDFs to ensure all document types can be summarised consistently.

Output Formatting and UI Planning

Defined clear output structure:

Title of Document

Key Points (bulleted)

Short summary in 3-4 lines

Discussed implementing Streamlit-based UI for internal testing to allow drag-and-drop PDF summarisation.

Successful End-to-End Summarisation

Verified that the pipeline:

Loads PDF.

Cleans and chunks text.

Summarises using LLM chunk-wise.

Generates a final merged summary.

Outputs structured JSON/text summary ready for Slack/email automation or UI presentation.

Confirmed accuracy and consistency for policy and marketing document summarisation use cases.

Problems Faced and Fixes

Problem Faced

Issue Fixed / Action Taken

Extracted PDF text contained repetitive headers/footers cluttering the input for summarisation.

Added regex-based post-processing to clean repetitive headers and footers from extracted text before passing to LLM.

Large document chunks exceeded LLM token limits, causing summarisation failures or cut-off outputs.

Implemented chunk-wise splitting with sentence overlap, summarising chunks individually and merging them for a final summary.

Faced JSONDecodeError due to unexpected response formats from LLM when parsing summarisation outputs.

Switched to using .get('response', '') safely during parsing, and ensured structured output requests in prompts to the LLM.

Scanned PDFs failed to extract text properly due to absence of OCR capability.

Planned integration of Tesseract OCR to extract text from scanned PDFs, ensuring all document types are handled consistently.

Encountered “port already in use” errors during test environment runs.

Identified existing processes using the port, avoided duplicate service restarts, and managed process cleanup when required.

Conclusion

This project enabled practical, hands-on experience in building a Document Summarisation Tool using LLMs with LangChain. The learning included effective PDF handling, chunking strategies, LLM prompt structuring, and planning UI integrations, ensuring the tool is functional, reliable, and ready for internal and client-facing summarisation workflows.
