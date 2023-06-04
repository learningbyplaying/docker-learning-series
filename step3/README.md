# Docker Learning Series

## How to build
sudo docker build -t step3 .

sudo docker run -v "$(pwd)/projects:/projects" \
                --user 1000:1000 \
                -it step3 bash run.sh  hola
