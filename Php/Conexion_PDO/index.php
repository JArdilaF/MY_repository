<?php
//diferencia con mysqli > se conecta a diversas bases de datos
try{
    $servidor = "localhost";
    $usuario = "root";
    $password = "";
    $bd = "primera_bd";
    $conexion = new PDO("mysql:host=$servidor; dbname=$bd", $usuario, $password);
    $nombre = "Maria";
    $apellido = "Romero";
    $sql = "INSERT INTO usuarios (nombre, apellido)
    VALUES (:nombre, :apellido)";
    $stmt = $conexion->prepare($sql);
    $stmt->bindParam(':nombre', $nombre);
    $stmt->bindParam(':apellido', $apellido);
    $stmt->execute();
echo "Usuario agregado con exito!!";
} catch (PDOException $th) {
    echo "Error: " . $th->getMessage();
}