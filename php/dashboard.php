
<HTML>
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script>
        $(document).ready(function() {
            $("button").click(function(){
                var dataId = $(this).attr("id");

                $.post("DisplayItems.php", {suggest: dataId}, function(result){
                    $("#contents").html(result);
                });
            });

            $("#po").click(function(){
                $.post("PlaceOrder.php",{suggest: 3} , function(result){
                    $("#contents").html(result);
                });      });
        });
    </script>
</head>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<BODY>
<div class="container"  style="background-color:#E6D3F2;">
    <div class="row" style="height: 5%; background-color:#D193F7; padding:40px;">
        <div class="col-12"></div>

    </div>
    <div class="row" style="height: 5%;background-color:#480673; color:#ffffff;">
        <div class="col-8"><h3>Gourmet Online Food Order</h3></div>
        <div class="col-2"><a href="#" id="po">Place Order</a></div>
        <div class="col-2"><a href="logout.php">Log Out <?php session_start(); echo $_SESSION['Uname'];?></a></div>
    </div>


    <div class="row" style="margin:25px;">

        <div class="shadow-sm p-3 mb-5 bg-white rounded">
            <div class="col-4" style="background-color:#ffffff; padding:40px; border-color:#230237; margin:20px;"></div>
            <?php
            $con=mysqli_connect("localhost","root","","foodorderdb");
            $qry="select * from menucategory_tbl";
            $run=mysqli_query($con,$qry);
            while ($rows=mysqli_fetch_array($run))
            {

                echo '<button id='.$rows['Category'].'><img src="image\\'.$rows['Category'].'.jpg" width="100px" height="100px"></button><br><blockquote class="blockquote text-center">'.$rows['CatDesc'].'</blockquote><br>';
            }
            ?>
        </div>

        <div class="col-8 shadow p-3 mb-5 bg-white rounded">
            <div class="col-8" id="contents" style="background-color:#ffffff; padding:40px; border-color:#230237; margin:20px;">
                <div class="card-columns">
                    <?php
                    $i=1;
                    $qry='select * from menuitems_tbl';
                    $run=mysqli_query($con,$qry);
                    while ($rows=mysqli_fetch_array($run))
                    {

                        echo '<div class="card" >';
                        echo '<img class="card-img-top" src="image\\'.$rows['MenuItemID'].'.jpg" height="120px" width="400px"  alt="'.$rows['ItemName'].'" >';
                        echo '<div class="card-body">';
                        echo '<p class="card-text">'.$rows['ItemName'].'</p>';
                        echo '<p class="card-text">$'.$rows['Price'].'</p>';
                        $key=$rows["MenuItemID"];
                        echo "<a href='AddToCart.php?ItemID=$key'><button type='button' class='btn btn-primary'>Buy</button></a>";
                        echo '</div></div>';

                        $i++;
                    }
                    ?>

                </div>

            </div>
        </div>
    </div>
</div>
</BODY>
</HTML>
