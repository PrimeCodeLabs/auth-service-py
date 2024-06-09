# Auth-Service

Auth-Service is a cloud-agnostic authentication service built with Python and FastAPI, designed to secure services and APIs. This service supports user authentication, token generation, and access control without using API keys. It incorporates rate limiting using Redis and includes a Docker setup for easy deployment.

## Features

- User authentication
- JWT token generation
- Secure access to protected endpoints
- Rate limiting using `slowapi` and Redis
- Dockerized for easy deployment

## Prerequisites

- Docker and Docker Compose
- Poetry (for dependency management)
- Python 3.9

## Getting Started

### Clone the Repository

git clone https://github.com/PrimeCodeLabs/auth-service-py.git
cd auth-service

### Setup Environment

Create a `.env` file in the `auth-service` directory with the following content:

```env
SECRET_KEY=your_secret_key
MONGO_URI=mongodb://mongodb:27017
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Install Dependencies

Use Poetry to install dependencies:

```bash
poetry install
```

### Build and Run with Docker Compose

```bash
docker-compose up --build
```

This will start the following services:

- `mongodb`: MongoDB instance
- `redis`: Redis instance for rate limiting
- `auth-service`: Authentication service exposed on port `8000`
- `secure-api`: Secure API service

### Running Tests

To run the tests, execute:

```bash
poetry run pytest
```

## API Endpoints

### Get Access Token

**Request:**

```bash
POST /token
Content-Type: application/x-www-form-urlencoded

username=admin&password=password
```

**Response:**

```json
{
  "access_token": "your_access_token",
  "token_type": "bearer"
}
```

### Get Current User

**Request:**

```bash
GET /users/me
Authorization: Bearer your_access_token
```

**Response:**

```json
{
  "username": "admin",
  "email": "admin@example.com"
}
```

## Rate Limiting

The service includes rate limiting to prevent abuse:

- **Login endpoint**: Limited to 5 requests per minute
- **Get current user endpoint**: Limited to 10 requests per minute

Rate limiting is implemented using `slowapi` with Redis as the backend.

## Deployment

### Cloud Deployment

You can deploy the service to any cloud provider that supports Docker, such as AWS, Azure, or GCP. Ensure that the environment variables are properly set and that MongoDB and Redis instances are accessible to the service.

### Local Deployment

For local development, use the provided `docker-compose.yml` to start all services. Ensure Docker and Docker Compose are installed on your machine.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [slowapi](https://pypi.org/project/slowapi/)
- [Docker](https://www.docker.com/)
- [Poetry](https://python-poetry.org/)
