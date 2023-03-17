docker run \
  --rm -it \
  --gpus all \
  --shm-size=12gb \
  --network host \
  -w /home/user/nerfstudio \
  -v /mnt/ssd/sdfstudio:/home/user/nerfstudio \
  -v /mnt/hdd/data:/home/user/nerfstudio/data \
  -v /home/yousiki/.cache:/home/user/.cache \
  sdfstudio:latest \
  $@