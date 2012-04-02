<?
$UDID = $_GET['UDID'];

$url = 'http://YOUR DOMAIN OR IP HEAR!/verify.php?udid=' . $UDID;
$result = file_get_contents($url);

if ($result == "YES") {
	echo "<a href='ca.pem'>Click Hear To download Cert";
}
else {
   	echo "Access Denied!, your UDID is not in our database!";
}
