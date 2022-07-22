# prefect-dbt-cloud

```bash
python -m venv env # create virtual environment
source env/bin/activate
env/bin/python -m pip install --upgrade pip
pip install -r requirements.txt
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
python data_pipeline_demo.py
prefect orion start
```

Static Flow Visualization
> This may only work with prefect 1.0
https://docs.prefect.io/core/advanced_tutorials/visualization.html