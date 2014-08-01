<?php
	if(!isset($_COOKIE['loggedin'])){
		header("location:index.php");
	}
?>

<html>
	<SCRIPT LANGUAGE="JavaScript">
		<!--
		function autoLink()
		{
		location.href="../../index.html";
		}
		setTimeout("autoLink()",5000); 
		// -->
	</SCRIPT>
		<h1>Welcome!</h1>
		Jump back to TOP page in 5 sec...

		start shopping</br>
		<a href ="../../index.html">NOW!</a>
		</br>
		</br>	
		
		<a href="logout.php">Logout</a>
	</body>
</html>
