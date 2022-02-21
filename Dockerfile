FROM tensorflow/tensorflow:latest-gpu-jupyter

WORKDIR /tf

# Create ENV
# RUN apt-get update
# RUN apt-get install python3-venv -y
# ENV VIRTUAL_ENV=/tf/pos/venv
# RUN python -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# RUN ls /tf/pos/venv

# Install depedencies  
RUN python -m pip install -U ipykernel

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

# COPY jupyter_notebook_config.py jupyter_notebook_config.py
# RUN mv jupyter_notebook_config.py $HOME/.jupyter/jupyter_notebook_config.py

EXPOSE 6006
EXPOSE 8888