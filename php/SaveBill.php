
<?php
$con=mysqli_connect("localhost","root","","foodorderdb");
session_start();
$tt=explode(",", substr($_SESSION['cart'],1));
$qty=$_POST['Quantity'];
$prc=$_POST['Price'];
$nam= $_SESSION['Uname'];
$billAmt=0;
$qry="select max(OrderID) as maxid from Orders_tbl";
$oid=0;
$run=mysqli_query($con,$qry);
while ($rows=mysqli_fetch_array($run))
{
    $oid=$rows[0]+1;
}
$cnt =0;

for($cnt=0;$cnt<count($qty);$cnt++)
{
    $qry="Insert into orderdetails_tbl values ($oid,".$tt[$cnt].",".$qty[$cnt].",".$qty[$cnt]*$prc[$cnt].",0)";
    $billAmt=$billAmt+$qty[$cnt]*$prc[$cnt];
    mysqli_query($con,$qry);
}
$qry="Insert into Orders_tbl values ($oid,'".date("Y/m/d")."','".$nam."',$billAmt,0)";
if (mysqli_query($con,$qry)==TRUE)
{
    echo '<script> alert("Order Placed Successful");</script>';
    header('refresh:0;url=dashboard.php');
}
else
{
    echo '<script> alert("Please try again");</script>';
    header('refresh:0;url=dashboard.php');
}
?>
