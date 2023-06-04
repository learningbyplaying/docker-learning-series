# Docker Learning Series

## How to build
sudo docker build -t step2 .

## Attact /app and run test.py

sudo docker run -v "$(pwd)/app:/app" \
                -v "$(pwd)/projects:/projects" \
                -w /projects \
                --user 1000:1000 \
                -it step2 python aws/run.py

sudo docker run -v "$(pwd)/app:/app" \
                -v "$(pwd)/projects:/projects" \
                -w /app \
                --user 1000:1000 \
                -it step2 bash run.sh


sudo docker build -t step2 .

sudo docker run -v "$(pwd)/projects:/projects" \
                --user 1000:1000 \
                -it step2 bash run.sh
