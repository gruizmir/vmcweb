// Form validation - register form
toastr.options = {"positionClass": "toast-top-full-width"};
$('.form-register').validate({
  messages: {
    name: "Debes ingresar tu nombre",
    lastname: "Debes ingresar tu apellido",
    email: "Debes ingresar un email válido",
    app_name: "Debes ingresar un nombre válido",
    description: "Debes ingresar una descripción válida",
    leader: "Debes registrar un líder de equipo",
    person2: "Mínimo 3 integrantes",
    person3: "Mínimo 3 integrantes",
  },
});
