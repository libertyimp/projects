<?php

$name = readline("Please enter your name: ");
$age = readline("Please enter your age: ");

$today = date("Y");

$answer = $today - $age + 100;

echo ("\nHello, " . $name . " you will be 100 years old in the year: " . $answer . "\n");
