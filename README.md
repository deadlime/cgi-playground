# CGI playground

This is a complementary repository for the following blog post:

[TODO](TODO) (english)\
[TODO](TODO) (hungarian)

To start the test server run:

```shell
$ docker compose up -d
```

To stop the test server run:

```shell
$ docker compose down
```

Building the C code for CGI:

```shell
$ gcc test.c -o cgi-bin/test
```

Running the CGI scripts:

```shell
$ curl 'http://localhost:8081/cgi-bin/test.pl?foo=bar'
Hello, World.
[...]
```

Accessing the FastCGI server:

```shell
$ curl 'http://localhost:8081/fcgi-bin/foo/bar'
Params:
[...]
```

Accessing the SCGI server:

```shell
$ curl 'http://localhost:8081/scgi-bin/foo/bar'
Headers:
[...]
```
