.PHONY: tests

tests:
	ENV=prod python3 -m pytest -s tests/*
