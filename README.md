# htmx-test
let's to have amusements

based on: https://testdriven.io/blog/flask-htmx-tailwind/

## setup:

```
git clone git@github.com:alkc/htmx-test.git
cd htmx-test

conda create -n htmx-test python=3.11
conda activate htmx-test

pip install -r requirements.txt

pre-commit install

wget https://raw.githubusercontent.com/testdrivenio/flask-htmx-tailwind/master/todo.py
wget https://unpkg.com/htmx.org@1.7.0/dist/htmx.js

mv htmx.js ./static/src/htmx.js

wget -O ./static/hearts.svg http://samherbert.net/svg-loaders/svg-loaders/hearts.svg

tailwindcss -i ./static/src/main.css -o ./static/dist/main.css --minify
```
