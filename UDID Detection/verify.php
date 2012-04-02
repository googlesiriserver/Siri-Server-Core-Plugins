<?php

$error = '';

mysql_connect("127.0.0.1", "root", "PASSWORD HEAR!") or die(mysql_error()); 
mysql_select_db("auth") or die(mysql_error()); 

$udid = $_GET['udid'];

if(trim($udid) == '') {
    $error .= 'udid was not received.';
    }

if($error == '') {

$sql = "SELECT * FROM users WHERE udid_id='$udid'";
$result = mysql_query($sql);

$rowCheck = mysql_num_rows($result);

	if($rowCheck > 0) {
	while($row = mysql_fetch_array($result)) {
	
	echo "YES";
	
	}
	
	} else {
	
	echo "NO";
	
	}
	
}

// Not required	
//echo $error;



?>
