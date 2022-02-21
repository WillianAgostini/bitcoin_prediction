# tensorflow/tensorflow:latest-gpu-jupyter

nvidia-docker run -v $PWD:/tf --gpus all --device /dev/nvidia0 --device /dev/nvidia-uvm --device /dev/nvidia-uvm-tools --device /dev/nvidiactl  --rm --name tf1 -p 8888:8888 -p 6006:6006 my-tensorflow jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root --no-browser