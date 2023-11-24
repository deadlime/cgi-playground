# CGI playground

Related blog post:

[Technologies left behind](https://deadlime.hu/en/2023/11/24/technologies-left-behind/) (english)\
[Hátrahagyott technológiák](https://deadlime.hu/2023/11/24/hatrahagyott-technologiak/) (hungarian)

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
