document.getElementById('subscribeButton').addEventListener('click', function() {
  var form = document.getElementById('subscriptionForm');
  if (form.checkValidity()) {
    var modal = new bootstrap.Modal(document.getElementById('modalRegistro'));
    modal.show();
  } else {
    form.classList.add('was-validated');
  }
});


function validarRut(input) {
  var rut = input.value.trim();
  if (rut.length >= 9 && rut.length <= 10) {
    input.setCustomValidity('');
    return true;
  } else {
    input.setCustomValidity(' ');
    return false;
  }
  
}

function validarNombre(input) {
  var nombre = input.value.trim();
  if (nombre.length >= 3 && nombre.length <= 20) {
    input.setCustomValidity('');
    return true;
  } else {
    input.setCustomValidity(' ');
    return false;
  }
}

function validarEmail(input) {
  var email = input.value.trim();
  if (email.length >= 10 && email.length <= 30) {
    input.setCustomValidity('');
    return true;
  } else {
    input.setCustomValidity(' ');
    return false;
  }
}

function validarPassword(input) {
  var password = input.value.trim();
  if (password.length >= 8) {
    input.setCustomValidity('');
    return true;
  } else {
    input.setCustomValidity(' ');
    return false;
  }
}

function validarTelefono(input) {
  var telefono = input.value.trim();
  if (telefono.length >= 9 && telefono.length <= 12) {
    input.setCustomValidity('');
    return true;
  } else {
    input.setCustomValidity(' ');
    return false;
  }
}