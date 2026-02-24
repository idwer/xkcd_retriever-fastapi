all: run_fastapi

run_fastapi:
	fastapi dev xkcd_retriever.py
