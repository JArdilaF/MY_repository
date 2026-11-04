<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_FILES["archivo"])) {
        $archivo = $_FILES["archivo"]["name"];
        $temporal = $_FILES["archivo"]["tmp_name"];

        // Definir la ruta donde se guardará el archivo
        $rutaDestino = "misSubidos/" . $archivo;

        // Mover el archivo desde la ubicación temporal a la ruta de destino
        if (move_uploaded_file($temporal, $rutaDestino)) {
            echo "El archivo se ha subido correctamente.";
        } else {
            echo "Error al subir el archivo.";
        }
    } else {
        echo "No se ha seleccionado ningún archivo.";
    }
}