
<?php
$con=mysqli_connect("localhost","root","","foodorderdb");
$id=$_GET["key"];
$qry="delete from menuitems_tbl where MenuItemID=$id";
if (mysqli_query($con,$qry)==true)
{
    echo "<script> alert('Record Deleted');</script>";
    echo "<script> window.location='adminLogin.php';</script>";
}
?>

