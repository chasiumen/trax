<head>
<body>
<?php

#Uploaded File Directory
$filename = "../upload/" . $_FILES["file"]["name"];


#Set allowed File types
$allowedExts = array("gif", "jpeg", "jpg", "png");

#SPLIT files
$temp = explode(".", $_FILES["file"]["name"]);
$extension = end($temp);


#------CHECK file type and size
#File type: gif, jpeg, jpg, png
#File size: 300MB

#Check if the file as been saved on dirctory /temp
#if (is_uploaded_file($_FILES["file"]["tmp_name"])){
#    echo "yes!";
#    }
#else{
#    echo "Failed to upload.... :(";
#}


if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/jpg")
|| ($_FILES["file"]["type"] == "image/pjpeg")
|| ($_FILES["file"]["type"] == "image/x-png")
|| ($_FILES["file"]["type"] == "image/png"))
&& ($_FILES["file"]["size"] < 314572800)
&& in_array($extension, $allowedExts)){

	if ($_FILES["file"]["error"] > 0){
		echo "Return Code: " . $_FILES["file"]["error"] . "<br>";
	}
	else{
		echo "Upload: " . $_FILES["file"]["name"] . "<br>";
		echo "Type: " . $_FILES["file"]["type"] . "<br>";
		echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
		echo "Temp file: " . $_FILES["file"]["tmp_name"] . "<br>";		
		if (file_exists($filename)){
			echo $_FILES["file"]["name"] . " already exists. <br>";
		}

		else{
			if (move_uploaded_file($_FILES["file"]["tmp_name"], $filename)){
				echo "Stored in: " . $filename. "<br>";
			}
			else{
				echo "Failed to store...". $filename. "<br>";
			}
 		}
	}
}
else{
	echo "Invalid file";
}


#print "<img src=\"$filename\"/>";

print "<td style=\"border:1px solid #000000\"><img src=\"$filename\" width=\"100\" height=\"100\"></td>";
#print "<td style=\"border:1px solid #000000\"><img src=\"$array_img[$i]\" width=\"100\" height=\"100\"></td>";



#---------------EXECUTE PYTHON SCRITP--------------------
print ("<br><br>");
print ("<b>Executing python script...</b><br>");
#echo "Execute python script....<br>";
$command = escapeshellcmd('../script/test.py ' . $filename);
$output = shell_exec($command);
echo $output;

?>
<!-- ENG of PHP SCRIPTS -->


 
</body>
</head>
