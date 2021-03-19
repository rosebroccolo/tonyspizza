
<?php
$dd=$_GET['ItemID'];
session_start();
$_SESSION['cart']= $_SESSION['cart'].','.$dd;
echo "<script>alert('".$dd." added');</script>";
echo $_SESSION['cart'];
header('refresh:0;url=http://localhost:8088/foodorder/dashboard.php');
?>
