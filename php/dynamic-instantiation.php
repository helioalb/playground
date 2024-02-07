<?php

class Foo {
  public function bar() {
    echo 'Foo bar';
  }
}

$type = Foo::class;

$foo = new $type();

$foo->bar();
