FROM python
WORKDIR /app
COPY . .
RUN pip install flask python-dotenv pytest
CMD ["python", "app.py"]