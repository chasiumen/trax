<html>
<head>
</head>
<body>

<?php

#recived value from form submit
$user = $_POST["user"];
$pass = $_POST["pass"];
$email= $_POST["email"];

echo ("USER:". $user);
echo ("PASS:". $pass);
echo ("EMAIL:".$email);


#---------------EXECUTE PYTHON SCRITP--------------------
print ("<br><br>");
print ("<b>Executing python script...</b><br>");
#echo "Execute python script....<br>";
$command = escapeshellcmd('../networking/caller.py'). " ". $user. " ".  $pass. " ". $email;
print ("<b>$command </b>");
$output = shell_exec($command);
echo $output;
?>
<!-- ENG of PHP SCRIPTS -->


</body>


</html>
