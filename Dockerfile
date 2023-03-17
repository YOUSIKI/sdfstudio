FROM nerfstudio:latest

# metainformation
LABEL org.opencontainers.image.version = "0.1.12"
LABEL org.opencontainers.image.source = "https://github.com/yousiki/sdfstudio"
LABEL org.opencontainers.image.licenses = "Apache License 2.0"
LABEL org.opencontainers.image.base.name="docker.io/library/nvidia/cuda:11.8.0-devel-ubuntu22.04"

# Copy nerfstudio folder and give ownership to user.
ADD . /home/user/nerfstudio
USER root
RUN chown -R user /home/user/nerfstudio
USER 1000

# Install nerfstudio dependencies.
RUN cd /home/user/nerfstudio && \
    python3.10 -m pip install -e . && \
    cd ..

# Change working directory
WORKDIR /home/user/nerfstudio

# Install nerfstudio cli auto completion and enter shell if no command was provided.
CMD ns-install-cli --mode install && /bin/bash

