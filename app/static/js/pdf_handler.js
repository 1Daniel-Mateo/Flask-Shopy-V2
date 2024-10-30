// Llamar al endpoint que genera el PDF y abrirlo en una nueva pestaña
fetch('/ejemplo/generar_pdf')
    .then(response => {
        if (response.ok) {
            // Redirigir a la URL para abrir el PDF en una nueva pestaña
            window.open(response.url, '_blank');
        } else {
            console.error('Error al generar el PDF');
        }
    })
    .catch(error => console.error('Error:', error));
