![image](https://github.com/user-attachments/assets/17a2730e-daf0-4f1a-bd05-e8efca49242a)# AI Blog Generator

## Overview
The **AI Blog Generator** is a web-based application that utilizes AWS Bedrock to generate high-quality blog posts based on user-provided topics. Users can enter a topic, and the system will generate a well-structured blog within seconds.

## Features
- Generate AI-powered blog posts instantly.
- User-friendly interface with a simple input field and button.
- Fetches blog content dynamically using AWS API Gateway and AWS Lambda.
- Displays real-time feedback while generating content.
- Error handling for smooth user experience.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** AWS Lambda (Node.js/Python)
- **AI Model:** AWS Bedrock (Large Language Models)
- **API Gateway:** AWS API Gateway
- **Hosting:** AWS S3 / Local

## Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/ervishnucs/Blog_Generator.git
   cd Blog_Generator
   ```

2. **Run Locally**
   - Open `index.html` in a browser.

3. **Deployment**
   - Deploy backend using AWS Lambda and API Gateway.
   - Host frontend on AWS S3 or any static hosting service.

## Usage
1. Open the application in a web browser.
2. Enter a blog topic in the input field.
3. Click on the **Generate Blog** button.
4. Wait for the AI to generate the blog and display the content.
5. Copy and use the generated blog as needed.

## API Endpoint
- The AI Blog Generator fetches data from:
  ```
  https://api_gateway/dev/blog_generation
  ```
- The API expects a JSON request body:
  ```json
  {
    "blog_topic": "Your topic here"
  }
  ```
## GitHub Repository
[GitHub Link](https://github.com/ervishnucs/Blog_Generator)

## Blog Generator

![image](Screenshot 2025-03-18 225740)




