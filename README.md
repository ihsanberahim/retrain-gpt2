## Fine tuning on custom datasets

Reference:  ["Beginner’s Guide to Retrain GPT-2 (117M) to Generate Custom Text Content"](https://medium.com/@ngwaifoong92/beginners-guide-to-retrain-gpt-2-117m-to-generate-custom-text-content-8bb5363d8b7f)

## User Guide

* all command lines used
  ```
  python3 -m venv env
  source env/bin/activate
  pip install -r requirements.txt
  
  python pdftotext.py hadis-40.pdf hadis-40.txt

  python download_model.py 117M

  PYTHONPATH=src python encode.py hadis-40.txt hadis-40.npz
  
  PYTHONPATH=src python ./train.py --dataset hadis-40.npz --model_name 117M --run_name=v1
  ```
