# Docker Learning Series

## How to build
sudo docker build -t step1 .

## How to run
sudo docker run -it step1

## Attact /app and run test.py

sudo docker run -v "$(pwd)/app:/app" -w /app -it step1 python test.py
