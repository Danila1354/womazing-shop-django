document.addEventListener("DOMContentLoaded", function () {
  const phoneInputs = document.querySelectorAll('input[name="phone"]');
  phoneInputs.forEach((input) => {
    Inputmask({
      mask: "+7 (999) 999-99-99",
      showMaskOnHover: false,
      showMaskOnFocus: true
    }).mask(input);
  });
});
