#use python 3.14 base image 
FROM python:3.14-slim

#set working directory
WORKDIR /app

#copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy rest of the application code
COPY . .

#expose the application port
EXPOSE 8000

#command to start FastAPI application
CMD ["uvicorn","calculator:app","--host","0.0.0.0","--port","8000"]