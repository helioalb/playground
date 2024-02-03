<?php

class DbFake {
  public static function execute(string $query): string {
    return "Result of $query\n";
  }
}

interface Cache {
  function get(string $key): bool | string;
  function set(string $key, string $data): void;
}

class RedisFake implements Cache {
  private array $map;

  public function __construct() {
    $this->map = array();
  }

  public function get(string $key): bool | string {
    if (array_key_exists($key, $this->map))
      return $this->map[$key];

    return false;
  }

  public function set(string $key, string $data): void {
    $this->map[$key] = $data;
  }
}

class CacheManager {
  private Cache $cache;

  public function __construct(Cache $cache) {
    $this->cache = $cache;
  }

  public function fetch($key, $callback, $query) {
    $data = $this->cache->get($key);

    if ($this->isCached($data)) {
        echo "data is cached\n";
        return $data;
    }

    echo "data is NOT cached\n";
    $data = call_user_func($callback, $query);
    $this->cache->set($key, $data);

    return $data;
  }

  private function isCached($data) {
    return $data!== false;
  }
}

function call_key_1($cache) : string {
  return $cache->fetch('key1', function($query){ return DbFake::execute($query); },
  'SELECT * FROM xpto');
}



$redis = new RedisFake();
$cache = new CacheManager($redis);

echo call_key_1($cache);
echo call_key_1($cache);
