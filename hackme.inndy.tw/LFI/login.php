<?php
require('config.php');
if($_POST['user'] === 'admin' && md5($_POST['pass']) === 'bed128365216c019988915ed3add75fb') {
    echo $flag;
} else {
?>
<form action="?page=pages/login" method="post" role="form">
        <div class="form-group">
                <label for="user-i">User</label>
                <input type="text" class="form-control" id="user-i" placeholder="Username" name="user">
        </div>
        <div class="form-group">
                <label for="pass-i">Password</label>
                <input type="password" class="form-control" id="pass-i" placeholder="Password" name="pass">
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
</form>
<?php } ?>

