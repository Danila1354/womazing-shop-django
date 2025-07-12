document.addEventListener("DOMContentLoaded", function () {
  const input = document.querySelector('.product-card__quantity-input');
  const btnMinus = document.querySelector('.product-card__quantity-btn--minus');
  const btnPlus = document.querySelector('.product-card__quantity-btn--plus');

  input.addEventListener('keydown', function (e) {
    const allowedKeys = ['Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'Tab'];

    if (
      (e.key >= '0' && e.key <= '9') ||
      allowedKeys.includes(e.key)
    ) {
      return;
    }

    e.preventDefault();
  });

  btnPlus.addEventListener('click', () => {
    let current = parseInt(input.value, 10) || 1;
    input.value = current + 1;
  });

  btnMinus.addEventListener('click', () => {
    let current = parseInt(input.value, 10) || 1;
    if (current > 1) {
      input.value = current - 1;
    }
  });
});
