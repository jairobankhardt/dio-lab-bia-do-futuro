setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r src/requirements.txt

run:
	. .venv/bin/activate && streamlit run src/app.py