<?php

    $servidor = "localhost"; //Por defecto es localhost
    $usuario = "root"; //Por defecto es root
    $contraseña = ""; //Por defecto es vacío
    $BD = "primera_bd";//Nombre de la base de datos creada en phpMyAdmin

    $conexion = mysqli_connect($servidor, $usuario, $contraseña, $BD);

    $nombre = "Juan";
    $apellido = "Ardila";

    $sql = "INSERT INTO usuarios (nombre, apellido) 
            VALUES ('$nombre', '$apellido')";

    if (mysqli_query($conexion, $sql)) {
        echo "Usuario agregado correctamente!!";
    }else {
        echo "Error al agregar el usuario: " . mysqli_error($conexion);
    }

    mysqli_close($conexion);
