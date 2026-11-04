<?php
//Verifica si se recibieron datos por POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    echo"Se recibio de manera exitosa el formulario";
} else {
    echo "No se recibieron datos por POST.";
}