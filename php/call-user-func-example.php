<?php

function hello_without_return(string $name) : void {
    echo "Hello $name \n";
}

function hello_with_return(string $name) : string {
    return "Hello $name \n";
}

call_user_func('hello_without_return', 'Fulano');

echo call_user_func('hello_with_return', 'Fulano');

// Lambda function

echo call_user_func(function(string $name) : string {
  return "Hello $name \n";
}, 'Ciclano lambda');

