<html>
<body>
Thank you <?php echo $_POST["name"]; ?>
<br>
We will be repsonding Soon.

<?php
$contact = "jordan.fazio-nagy@sydney.edu.au";
/*switch ($_POST["matter"]){
	case "registration":
		$contact = "jordan.fazio-nagy@sydney.edu.au";
	break;
	case "resources":
		$contact = "jordan.fazio-nagy@sydney.edu.au";
	break;
	case "general"
		$contact = "jfaz5011@uni.sydney.edu.au";
	break;
	default:
		$contact = "jordan.fazio-nagy@sydney.edu.au";
}
*/
mail($contact,"Subject: ". $_POST["matter"],"\n Name: " . $_POST["name"]. "\n\n".$_POST["querybody"]);
//$_POST["email"] = "nil";?>

</body>
</html>
