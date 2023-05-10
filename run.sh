python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

python pdftotext.py document.pdf document.txt

python download_model.py 117M

PYTHONPATH=src python encode.py document.txt document.npz

PYTHONPATH=src python ./train.py --dataset document.npz --model_name 117M --run_name=brian_hocklai
PYTHONPATH=src python ./train.py --dataset document.npz --model_name 117M --run_name=brian_esan

python ./src/interactive_conditional_samples.py --temperature 0.8 --top_k 40 --model_name v1