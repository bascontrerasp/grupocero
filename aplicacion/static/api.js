fetch('https://worldtimeapi.org/api/ip')
    .then(response => response.json())
    .then(data => {
      const hora = new Date(data.datetime);
      const horaFormateada = hora.toLocaleTimeString();
      document.getElementById('hora-actual').innerText = `Hora actual: ${horaFormateada}`;
    })
    .catch(error => {
      console.error('Error al obtener la hora:', error);
    });