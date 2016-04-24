.PHONY: build clean
build: gitoverview_code.py gitoverview_utils.py
	cat $^ > gitoverview.py

clean:
	rm gitoverview.*
