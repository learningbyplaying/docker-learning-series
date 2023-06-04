# Docker Learning Series

## How to build
sudo docker build -t step2 .

## Attact /app and run test.py

sudo docker run -v "$(pwd)/app:/app" \
                -v "$(pwd)/projects:/projects" \
                -w /projects \
                -it step2 python aws/run.py
