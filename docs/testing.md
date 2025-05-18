1. Run the application
   make run

2. Test the API endpoint using curl
   curl -X GET "http://localhost:8000/api/v1/example/example"

3. Check the health endpoint:
   curl -X GET "http://localhost:8000/health"

4. Better way to test (Swagger UI)
   http://localhost:8000/docs

5. Stop
   ps aux | grep "uvicorn app.main" | grep -v grep | awk '{print $2}' | xargs kill

6. Docker Testing

   # Build the Docker image

   make docker-build

   # Run the Docker container with environment variables

   docker run -d -p 8000:8000 \
    -e APP_NAME=python-template \
    -e ENVIRONMENT=development \
    -e DEBUG=True \
    -e LOG_LEVEL=INFO \
    -e SECRET_KEY=test-key \
    -e ENABLE_DOCS=True \
    -e ENABLE_CORS=True \
    python-microservice:latest

   # Check if container is running

   docker ps

   # Test endpoints (same as above)

   curl -X GET "http://localhost:8000/health"
   curl -X GET "http://localhost:8000/api/v1/example/example"

   # Access Swagger UI

   http://localhost:8000/docs

   # Stop Docker container

   docker stop <container_id>
