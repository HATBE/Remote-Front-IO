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
            exec('python ../power.py power');
            break;
        case 'powerhard':
            exec('python ../power.py powerhard');
            break;
        case 'reset':
            exec('python ../power.py reset');
            break;
        default:
            dir('unknown error (no valid action)');
            break;
    }