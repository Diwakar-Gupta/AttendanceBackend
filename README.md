# attendance-backend


## Setup

### To build an image.
```bash
docker build -t attendance-backend .
```

### To run the container and listen on localhost.
```bash
docker run --network=host attendance-backend
```

Now you can access the server at `http://localhost:8000`

if anything is missed visit [docker-cheetsheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)

## To run test file

### To run all test
```bash
python manage.py test
```
### To run a specific testfile
```bash
python manage.py test attendance.test.models.test_classattendancewithgeolocationTest
```