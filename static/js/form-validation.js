// Form validation - register form
    toastr.options = {"positionClass": "toast-top-full-width"};
    $('.form-register').validate({
      messages: {
        name: "Debes ingresar un nombre para el equipo",
        email: "Debes ingresar un email válido",
        phone: "Debes ingresar un teléfono válido",
        leader: "Debes registrar un líder de equipo",
        person2: "Mínimo 3 integrantes",
        person3: "Mínimo 3 integrantes",
      },
    });