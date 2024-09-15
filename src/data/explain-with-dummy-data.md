To explain the given code in detail, we'll break it down and provide a hypothetical example with some dummy data.

### Code Overview

The code defines a `DocumentProcessor` class that reads text files from a specified directory, processes each file to extract sentences, and returns a list of dictionaries containing these sentences and their source filenames. It uses `nltk` for sentence tokenization and `ThreadPoolExecutor` for concurrent file processing.

### Key Components

1. **Imports:**
   - `os`: Used for directory and file path operations.
   - `nltk`: Provides natural language processing tools; here, it’s used for sentence tokenization.
   - `ThreadPoolExecutor`: Allows concurrent execution of file processing to speed up the task.
   - `List`, `Dict`: Type hints for better code readability and maintenance.

2. **NLTK Setup:**
   - Downloads the 'punkt' tokenizer model quietly, which is necessary for sentence tokenization.

3. **DocumentProcessor Class:**
   - **`__init__`:** Initializes with the path to the directory containing text documents.
   - **`process_documents`:** 
     - Iterates over files in the directory, submitting tasks to process each `.txt` file concurrently.
     - Collects processed results as they complete.
   - **`_process_file`:** 
     - Reads the content of a file.
     - Tokenizes the content into sentences.
     - Filters and stores sentences longer than 10 characters with their source filename.

### Example with Dummy Data

Suppose the `documents_dir` contains the following text files:

- **file1.txt**:
  ```
  This is the first document. It contains multiple sentences. Here is another sentence.
  ```

- **file2.txt**:
  ```
  Short. This document has more content. We need to extract sentences.
  ```

### Step-by-Step Execution

1. **Initialization:**
   ```python
   processor = DocumentProcessor(documents_dir='path/to/documents')
   ```

2. **Processing Documents:**
   - The `process_documents` method lists files in the directory and uses a thread pool to process each `.txt` file concurrently.
   - For each file, `_process_file` is called.

3. **File Processing:**
   - **file1.txt:**
     - Reads content.
     - Tokenizes: ["This is the first document.", "It contains multiple sentences.", "Here is another sentence."]
     - Filters: All sentences are longer than 10 characters.
     - Returns:
       ```python
       [{'text': 'This is the first document.', 'source': 'file1.txt'},
        {'text': 'It contains multiple sentences.', 'source': 'file1.txt'},
        {'text': 'Here is another sentence.', 'source': 'file1.txt'}]
       ```

   - **file2.txt:**
     - Reads content.
     - Tokenizes: ["Short.", "This document has more content.", "We need to extract sentences."]
     - Filters: "Short." is ignored (less than 10 characters).
     - Returns:
       ```python
       [{'text': 'This document has more content.', 'source': 'file2.txt'},
        {'text': 'We need to extract sentences.', 'source': 'file2.txt'}]
       ```

4. **Collecting Results:**
   - The `process_documents` method aggregates results from all futures, resulting in:
     ```python
     [
       {'text': 'This is the first document.', 'source': 'file1.txt'},
       {'text': 'It contains multiple sentences.', 'source': 'file1.txt'},
       {'text': 'Here is another sentence.', 'source': 'file1.txt'},
       {'text': 'This document has more content.', 'source': 'file2.txt'},
       {'text': 'We need to extract sentences.', 'source': 'file2.txt'}
     ]
     ```

### Conclusion

This implementation efficiently processes multiple text files in parallel, extracting relevant sentences and associating them with their source files. This is useful for applications like text analysis, data preprocessing, or document indexing.