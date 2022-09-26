# For more information, please refer to https://aka.ms/vscode-docker-python
FROM openstax/selenium-chrome

WORKDIR /app

# Install pip requirements
COPY . .

# python -m pip install -r requirements.txt
RUN pip3 install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3", "main.py"]
