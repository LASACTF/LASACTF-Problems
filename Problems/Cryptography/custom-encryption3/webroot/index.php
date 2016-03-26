<html>
<body>
<form action="index.php" method="POST">
Log entry: <input type="text" name="entry" />
<input type="submit" value="Log">
</form>
<?php
  include "config.php";

  function encrypt($key, $message) {
    $key1 = 0;
    $key2 = 0;
    $key3 = 0;
    for ($i = 0; $i < 4; $i++) {
      $key1 *= 256;
      $key2 *= 256;
      $key3 *= 256;
      $key1 += ord($key[$i]);
      $key2 += ord($key[$i + 4]);
      $key3 += ord($key[$i + 8]);
    }
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
        $in += $part;
      }
      $in *= $key1;
      $in = (($in & 0xFFFFFF00) >> 8) | (($in & 0xFF) << 24);
      $in *= $key2;
      $in = (($in & 0xFF000000) >> 24) | (($in & 0xFFFFFF) << 8);
      $in *= $key3;
      $in &= 0xFFFFFFFF;
      
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
