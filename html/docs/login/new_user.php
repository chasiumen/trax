<?php
#	$username = "chasiumen";
#	$password = "agumion$)0822";
#	$hostname = "192.168.1.147";
#	
#	//$dbhandle = mysql_connect($hostname, $username, $password) or die("Could not connect to database");
#	
#	$dbhandle = mysql_connect('192.168.1.147', 'chasimen', 'agumion$0822') or die("Could not connect to database");	
#	$selected = mysql_select_db("test", $dbhandle);
#	
#		if(isset($_POST['user']) && isset($_POST['pass'])){
#			$user = $_POST['user'];
#			$pass = $_POST['pass'];
#
#			$query = mysql_query("SELECT * FROM USERS WHERE login_name='$user'");
#			if(mysql_num_rows($query) > 0 ) { //check if there is already an entry for that username
#			echo "<font size='3' color='#ED1A3'><b>$user</b> already exists!</font>";
#			}else{
#				mysql_query("INSERT INTO USERS (login_name, pass) VALUES ('$user', '$pass')");
#				header("location:../login.html");
#			}
#	}
#	mysql_close();
?>

<html>
	<body>
		<h1>Signup!</h1>
			<form action="new_user.php" method="POST">
				<p>Username:</p><input type="text" name="user" />
				<p>Password:</p><input type="password" name="pass" />
				<br />
				<input type="submit" value="Signup!" />
			</form>
	</body>
</html>
