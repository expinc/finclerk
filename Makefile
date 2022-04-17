.PHONY: clean test

clean:
	rm -rf tmp
	find . -name "__pycache__" | xargs rm -rf

test:
	sh bin/test.sh
