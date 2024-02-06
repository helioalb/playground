<?php

class Db
{
    private $dbname;
    private static $instance;

    public static function getInstance()
    {
        if (isset(self::$instance)) {
            echo 'Reuse instance -> ';
            return self::$instance;
        }

        echo 'Create new instance -> ';
        self::$instance = new Db();

        return self::$instance;
    }

    private function __construct($dbname = 'foo')
    {
        $this->dbname = $dbname;
    }

    public function execute($sql)
    {
        return "$sql executed on database $this->dbname\n";
    }
}

echo Db::getInstance()->execute('SELECT 1');
echo Db::getInstance()->execute('SELECT 2');
echo Db::getInstance()->execute('SELECT 3');
