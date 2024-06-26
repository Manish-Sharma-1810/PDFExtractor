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
- **Gunicorn:** Python WSGI HTTP server for running Python applications, including Flask, in a production environment.
- **AWS Services:**
  - **S3:** Storage service used for storing uploaded PDFs and extracted JSON files.
  - **SQS:** Message queue service for decoupling and asynchronous processing.
  - **Lambda:** Serverless compute service used for content extraction.
  - **CloudWatch:** Monitoring and logging service for application health and performance metrics.
  - **CloudFormation:** Infrastructure as Code service for provisioning and managing AWS resources.
  - **VPC (Virtual Private Cloud):** Isolated virtual network in the AWS cloud.
  - **Public Subnets:** Subnets with routes to the internet gateway for resources that need to be publicly accessible.
  - **Internet Gateway:** Allows communication between instances in the VPC and the internet.
  - **Route Tables:** Controls the flow of network traffic within and in/out of an AWS VPC, enabling secure and efficient communication between resources within the VPC and with external networks.
  - **Network ACLs (Access Control Lists):** Acts as a firewall for controlling traffic in and out of one or more subnets.
  - **Security Groups:** Acts as a virtual firewall for the associated AWS resources, controlling inbound and outbound traffic.
  - **Application Load Balancer:** Distributes incoming application traffic across multiple targets, such as Amazon EC2 instances.
  - **Route53:** Domain Name System (DNS) web service for routing traffic to various AWS resources.
- **Docker:** Containerization platform for packaging the Flask application and its dependencies.
- **Nginx:** Web server and reverse proxy server for handling client requests listening on port 80, and routing them to Flask application containers.


# Instructions to deploy Flask application on EC2

### **Note:**
 replace the ***dev-flask-lab*** with your own ***BUCKET_NAME***

### 1. Clone Repository:
```
git clone https://github.com/Manish-Sharma-1810/PDFExtractor.git
```

### 2. Create s3 bucket
```
aws s3api create-bucket --bucket dev-flask-lab --region us-east-1
```

### 3. Copy the code to s3 bucket
```
aws s3 cp ./PDFExtractor/ s3://dev-flask-lab/PDFExtractor/ --recursive && \
aws s3 cp ./Deployment/ s3://dev-flask-lab/templates/ --recursive
```

### 4. Create CloudFormation stacks for the application
```
aws cloudformation create-stack --stack-name app --template-url https://dev-flask-lab.s3.amazonaws.com/templates/app.yaml --parameters ParameterKey=DeploymentBucket,ParameterValue=dev-flask-lab --capabilities CAPABILITY_NAMED_IAM --region us-east-1
```

### 5. Check app stack status
```
aws cloudformation describe-stacks --stack-name app --query "Stacks[0].StackStatus" --output text --region us-east-1
```
### 6. Check app stack outputs
```
aws cloudformation describe-stacks --stack-name app --query "Stacks[0].Outputs" --output table --region us-east-1
```