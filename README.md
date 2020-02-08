# Garage Demo

The _Garage_ is a RESTful API based on an OpenApi specification `spec/garage.openapi.yml`.

The project is based on the generated server stub of the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. The code generated from the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

The persistence layer makes intentionally no use of an ORM to show transaction handling and some advanced SQL statements.

## Roadmap

- [x] implement `decimal` format validation where swagger-codegen falls short
- [x] provide default value for `garage.date_created`, ensure ISO8601 format
- [x] generate fixtures using https://mockaroo.com
- [x] enforce foreign keys in sqlite settings for integrity and cascading deletions
- [x] create database index on `car.price` for faster comparisons
- [ ] centralize api response error codes and messages
- [ ] pickup host from the API spec and add CORS headers
- [ ] implement integration tests, coverage and setup travis CI hook
- [ ] move over to a postgresql database
- [ ] use gunicorn as a pre-fork production server
- [ ] setup an nginx reverse-proxy in front of it
- [ ] docker-compose all of the containers

## Development

Set up the environnement, create the sqlite database and run the development server:
```sh
pip install pipenv
pipenv --python 3.6
pipenv install
pipenv shell
(env)$ python -m database        # [re]creates the database
(env)$ python -m swagger_server  # may need patch for package `connexion`, see troubleshooting section
```
Then open your browser at http://localhost:8080/garage/api/1.0.0/ui/

## Testing
To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Containerization

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t demo-garage .

# starting up a container, daemonized
docker run -d -p 8080:8080 demo-garage
```

## Troublshooting

### Faulty dependencies
Upon launching the server `python -m swagger_server` you get the following warning:
```
ImportError: cannot import name 'FileStorage'
```
The fix is already under way in package `connexion@1.1.16`. Quick fix it in python's `lib/site-packages/connexion/decorators/validation.py` with the following
```diff
- from werkzeug import FileStorage
+ from werkzeug.datastructures import FileStorage
```

### Enforce Foreign Keys
Sqlite does not enforce foreign keys by default. The setting can be changed using the following command:
```sql
PRAGMA foreign_keys = ON;
```
However, the sqlite installation needs to have been compiled with certain flags (see the [docs](https://sqlite.org/foreignkeys.html)) for the setting to persist and take effect. To circumvent this shortcoming, the above command can be issued with every new connection.