FROM python
WORKDIR /app
COPY . .
RUN pip install flask python-dotenv
CMD ["python", "app.py"]