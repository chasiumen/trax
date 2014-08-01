<html>
<body>

<p> OUTPUT </p>
<?php
	echo $_POST["param"], "</br>";
	$base="http://chasiumen.net/index.html";
	
	$url =$base. $_POST["param"];
#	echo $url;
#	header("HTTP/1.1 301 Moved Permanently");
	header("Location: $url");
	exit;
?>


</body>
</html>
