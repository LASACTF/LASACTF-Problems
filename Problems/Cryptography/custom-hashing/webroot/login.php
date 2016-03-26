<?php
  include "config.php";
  
  function super_strong_hash($pass) {
    $state = array(13, 73, 54, 23, 37, 45, 103, 81);
    for ($i = 0; $i < strlen($pass); $i += 8) {
      for ($j = 0; $j < 8; $j++) {
        if ($i + $j < strlen($pass)) {
          $state[$j] ^= ord($pass[$i + $j]);
        }
      }
      $state[4] += $state[0];
      $state[4] %= 128;
      $state[5] += $state[1];
      $state[5] %= 128;
      $state[6] += $state[2];
      $state[6] %= 128;
      $state[7] += $state[3];
      $state[7] %= 128;
      
      $state[1] ^= $state[0];
      $state[3] ^= $state[2];
      $state[5] ^= $state[4];
      $state[7] ^= $state[6];

      $state[0] *= 13;
      $state[0] %= 128;
      $state[1] *= 13;
      $state[1] %= 128;
      $state[2] *= 13;
      $state[2] %= 128;
      $state[3] *= 13;
      $state[3] %= 128;
      $state[4] *= 13;
      $state[4] %= 128;
      $state[5] *= 13;
      $state[5] %= 128;
      $state[6] *= 13;
      $state[6] %= 128;
      $state[7] *= 13;
      $state[7] %= 128;
    }
    return chr($state[0]) . chr($state[1]) . chr($state[2]) . chr($state[3]) . chr($state[4]) . chr($state[5]) . chr($state[6]) . chr($state[7]);
  }
  
  $con = new SQLite3($database_file);
  $username = $_POST["username"];
  $password = $_POST["password"];
  $password_hash = super_strong_hash($password);
  $query = "SELECT * FROM users WHERE name='$username' AND password_hash='$password_hash'";
  $result = $con->query($query);
  $row = $result->fetchArray();
  if ($row) {
    echo "<h1>Logged in!</h1>";
    echo "<p>Your flag is: $FLAG</p>";
  } else {
    echo "<h1>Login failed.</h1>";
  }
?>
