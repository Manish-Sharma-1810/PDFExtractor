# PDFExtractor

**PDFExtractor:** A Flask application leveraging AWS services for seamless extraction of content from PDF files, serving customers asynchronously.

## Introduction

PDFExtractor is a Flask application integrated with various AWS services to streamline the process of extracting content from PDF files and storing them in JSON format. This project allows users to upload PDF files to an S3 bucket, triggering an SQS message. The SQS message then triggers an AWS Lambda function, which retrieves the PDF file from the S3 location specified in the message, extracts the content (paragraphs, headers, embedded links), and saves it into a JSON file. Finally, the JSON file is uploaded back to an S3 bucket.

## Features

- **PDF Upload:** Users can easily upload PDF files through a simple web interface.
- **Asynchronous Processing:** SQS queues are used to decouple file uploads from content extraction, allowing for efficient and scalable processing.
- **Serverless Processing:** AWS Lambda functions handle the extraction of content, triggered by SQS messages upon PDF uploads to S3.
- **Content Extraction:** The Lambda function extracts paragraphs, headers, and embedded links from the uploaded PDF files.
- **JSON Storage:** Extracted content is stored in JSON format on Amazon S3 for easy retrieval and further processing.

## Technologies Used

- **Python Flask:** Web framework for building the application backend.
- **AWS Services:**
  - **S3:** Storage service used for storing uploaded PDFs and extracted JSON files.
  - **SQS:** Message queue service for decoupling and asynchronous processing.
  - **Lambda:** Serverless compute service used for content extraction.
  - **CloudWatch:** Monitoring and logging service for application health and performance metrics.
- **Docker:** Containerization platform for packaging the Flask application and its dependencies.

## Usage

### Clone Repository:
```
git clone https://github.com/Manish-Sharma-1810/PDFExtractor.git
```

### Create a python virtual environment
```
python3 -m venv venv
```

### Activate the virtual environment
```
source venv/bin/activate
```

### Install dependencies
```
pip3 install -r requirements.txt
```