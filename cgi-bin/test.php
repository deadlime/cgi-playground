#!/usr/bin/php82
<?php

print("Content-Type: text/plain\n\nHello World!\n");

print("\nEnvironment:\n");
var_dump($_SERVER);

print("\nInput:\n");
var_dump(file_get_contents('php://stdin'));
