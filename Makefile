.PHONY: clean init test run

clean:
	rm -rf tmp
	find . -name "__pycache__" | xargs rm -rf

init:
	sh bin/init.sh

test:
	sh bin/test.sh

run:
	sh bin/run.sh
