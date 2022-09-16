<?php
    if($_SERVER['REQUEST_METHOD'] !== 'POST') {
        die('Please use the requestmethod POST');
    }
    if(!isset($_POST['action'])) {
        die('Please specify a action');
    }

    $action = htmlentities($_POST['action']);

    $validActions = ['power', 'powerhard', 'reset'];

    if(!in_array($action, $validActions)) {
        die('Please use a valid action');
    }

    switch ($action) {
        case 'power':
            exec('sudo /usr/bin/python /var/www/html/power.py power');
            break;
        case 'powerhard':
            exec('sudo /usr/bin/python /var/www/html/power.py powerhard');
            break;
        case 'reset':
            exec('sudo /usr/bin/python /var/www/html/power.py reset');
            break;
        default:
            dir('unknown error (no valid action)');
            break;
    }