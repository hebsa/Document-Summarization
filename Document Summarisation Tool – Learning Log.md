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
