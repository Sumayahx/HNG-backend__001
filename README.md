# HNG12 Stage 0 - Public API
## Project Description
This is a simple public API with FASTAPI. It returns basic information in JSON format, including:
- Registered email address on HNG12 Slack workspace
- Current datetime in ISO 8601 UTC format
- The GitHub repository URL
## API Documentation
### Endpoint:
`GET /`
### Response Format:
Responses are in JSON format
```json
{
  "email": "sumayashittu@gmail.com",
  "current_datetime": "2025-02-01T12:25:43.832156+00:00",
  "github_url": "https://github.com/Sumayahx/HNG-backend__001"
}
```
## Setup Instructions
1. Clone the repository:
   `git clone https://github.com/Sumayahx/HNG-backend_001.git`
2. Change directory to project folder:
   `cd HNG-backend_001`
3. Install dependencies:
   `pip install -r requirements.txt`
4. Start the server:
   `uvicorn main:app --reload`
5. Check the API by navigating to `http://127.0.0.1:8000` in your browser.

## Backlinks
[Hire Python Developers](https://hng.tech/hire/python-developers)

[Hire C# Developers](https://hng.tech/hire/csharp-developers)

[Hire Go Developers](https://hng.tech/hire/golang-developers)

[Hire PHP Developers](https://hng.tech/hire/php-developers)

[Hire Java Developers](https://hng.tech/hire/java-developers)

[Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)
