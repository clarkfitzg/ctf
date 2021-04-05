install: 
	python3 -m pip install --user --upgrade build 
	python3 -m build 
	pip3 install dist/column_text_format-0.0.2-py3-none-any.whl --user --upgrade
