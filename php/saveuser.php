
<?php
$con=mysqli_connect("localhost","root","","foodorderdb");
$un=$_POST["username"];
$pwd=$_POST["password"];
$phno=$_POST["phoneno"];
$eml=$_POST["email"];
$dadd=$_POST['DeliAdd'];
$cty=$_POST['city'];
$utype="user";
$qry="Insert into Users_tbl values ('$un','$pwd','$utype','$phno','$eml','$dadd','$cty')";
if (mysqli_query($con,$qry)==TRUE)
{
    echo '<script> alert("Successful");</script>';
    header('refresh:0;url=HomePage.html');
}
else
    echo '<script> alert("Please try again");</script>';
?>
