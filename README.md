"# python-package-flask-test" 

## Lauch the app
- py runserver

## Endpoint
- http://localhost:5000/api/v1/customers/

## Test execution
- py -m unittest discover -s tests/unit -v
- py -m unittest discover -s tests/acceptance -v

## Build package
- py -m build

## Publish package
- twine upload  --repository-url http://localhost:8081/repository/hosted-python/ dist/* -u${USER} -p${USERPASS}
