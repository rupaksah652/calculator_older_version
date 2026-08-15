#use python 3.14 base image 
FROM python:3.14-slim

#set working directionary
WORKDIR /app

#copy reqirement and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy rest of the appliocation code
COPY . .

#expose the appliocation part
EXPOSE 8000

#command to start FastAPI application
CMD ["uvicorn","calculator:app","--host","0.0.0.0","--port","8000"]