# e-cached
An experimental in-memory cache db

## Goals
A side project required a fast read/write layer. While there exist many open source in-memory cache systems such as Redis or memcached, I want to better understand how they work and how an in-memory cache can be implemented. I will implement this project using Go and Python 3. I consider this a great learning experience both in terms of understanding an in-memory cache and learning Go.

## Dev Guide
###Python version
After repo checkout, the Python cached is under the `py_cached` directory. It follows mostly the Pythonic coding style and uses the Python package setup and a Makefile to run tests.

### Go version
The Go version is under the `go_cached` directory. The Dockerfile will move the source code to the proper Go workspace defined in the `go-dev` docker image. The parent Makefile that builds the Docker container will trigger `go test` so there is no Makefile in the `go_cached` directory. Unit test for each package is in the same directory as the source code of that package.

### Testing
To run tests, go to the project root directory `e-cached` and run `make`

## Reference
- Golang code structure: https://talks.golang.org/2014/organizeio.slide#1
- Unit test reference:
https://blog.alexellis.io/golang-writing-unit-tests/
- Another unit test reference: http://smartystreets.com/blog/2015/02/go-testing-part-2-running-tests
