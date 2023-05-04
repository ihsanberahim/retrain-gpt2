python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python pdftotext.py hadis-40.pdf hadis-40.txt
PYTHONPATH=src python encode.py hadis-40.txt hadis-40.npz
PYTHONPATH=src python ./train.py --dataset hadis-40.npz --model_name 117M --run_name=v1