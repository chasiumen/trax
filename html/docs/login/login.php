<?php
	$username = "tbd";
	$password = "arc0326";
	$hostname = "chasiumen.net";
	
	//$dbhandle = mysql_connect($hostname, $username, $password) or die("Could not connect to database");
	
	$dbhandle = mysql_connect('chasiumen.net', 'tbd', 'arc0326') or die("Could not connect to database");
	
	$selected = mysql_select_db("tbd", $dbhandle);
	
	$myusername = $_POST['user'];
	$mypassword = $_POST['pass'];
	
	$myusername = stripslashes($myusername);
	$mypassword = stripslashes($mypassword);
	
	$query = "SELECT * FROM USERS WHERE login_name='$myusername' and pass='$mypassword'";
	$result = mysql_query($query);
	$count = mysql_num_rows($result);
	
	mysql_close();
	
	if($count==1){
		$seconds = 5 + time();
		setcookie(loggedin, date("F jS - g:i a"), $seconds);
		header("location:login_success.php");
	}else{
		echo 'Incorrect Username or Password';
	}
?>