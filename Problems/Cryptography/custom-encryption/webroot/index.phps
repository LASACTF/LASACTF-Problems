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
      $in = 0;
      for ($j = 0; $j < 4; $j++) {
        $in *= 256;
        if ($i + $j < strlen($message)) {
          $part = ord($message[$i + $j]);
        } else {
          $part = 0;
        }
        $part ^= ord("encrypt!"[$j]);
        $in += $part
      }
      $in *= $key;
      $in = (($in & 0xFF000000) >> 24) | (($in & 0xFF0000) >> 8) | (($in & 0xFF00) << 16) | (($in & 0xFF) << 16);
      $in *= $key;
      $in = (($in & 0xFF000000) >> 24) | (($in & 0xFF0000) >> 8) | (($in & 0xFF00) << 8) | (($in & 0xFF) << 24);
      $in *= $key;
      $in = (($in & 0xFF000000) >> 8) | (($in & 0xFF0000) >> 8) | (($in & 0xFF00) >> 8) | (($in & 0xFF) << 24);
      $in += $key;
      
      $out .= chr($in & 0xFF);
      $out .= chr(($in & 0xFF00) >> 8);
      $out .= chr(($in & 0xFF0000) >> 16);
      $out .= chr(($in & 0xFF000000) >> 24);
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
