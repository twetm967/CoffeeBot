<?php
	
    if ($_GET['pin'] == 2)
    {		
	 exec('sudo python3 coffee.py 7 1');
    }
    else if ($_GET['pin'] == 1)
    {
          exec('sudo python3 coffee.py 7 0');
    }
    
echo '
<html>
	<head>
		<title>Coffee Controller</title>
	</head>
<body>
    <form method="post">
    <div style="width: 100%; height: 100%; text-aling: center;">
    <p>
	   <a href="coffee.php?pin=2" style="text-decoration: none; color: #000000;">     
		<img src="on.jpg" border="0" height="700" width="700">
    </p>
    <p>
        <a href="coffee.php?pin=1" style="text-decoration: none; color: #000000;">     
		<img src="off.png" border="0" height="700" width="700">
    </p>
    </form>
</body>
</html>
'
?>
