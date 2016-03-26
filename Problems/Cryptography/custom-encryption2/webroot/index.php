<html>
<body>
<form action="index.php" method="POST">
Log entry: <input type="text" name="entry" />
<input type="submit" value="Log">
</form>
<?php
  include "config.php";

  function encrypt($key, $message) {
    $out = "";
    for ($i = 0; $i < strlen($message); $i += 4) {
      $in = array();
      for ($j = 0; $j < 4; $j++) {
        if ($i + $j < strlen($message)) {
          $in[j] = ord($message[$i + $j]);
        } else {
          $in[j] = 0;
        }
      }
      $in[3] += 3 * $in[1];
      $in[0] += $in[2];
      $in[1] += $in[2] + $in[0];
      $out_arr = array(0, 0, 0, 0);
      for ($j = 0; $j < 4; $j++) {
        for ($k = 0; $k < 4; $k++) {
          $out_arr[$j] += ord($key[$j * 4 + $k]) * $in[$k];
        }
        $out_arr[$j] %= 251;
      }
      
      $out .= chr($out_arr[0]);
      $out .= chr($out_arr[1]);
      $out .= chr($out_arr[2]);
      $out .= chr($out_arr[3]);
    }
    return $out;
  }
  
  if (isset($_POST["message"])) {
     echo "Encrypted: ";
     echo base64_encode(encrypt($FLAG, $_POST["message"]));
     echo "<br />";
  }
?>
<a href="index.phps">Source</a>
</body>
</html>
