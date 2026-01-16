document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.product-card__quantity-wrapper').forEach(wrapper => {
        const input = wrapper.querySelector('.product-card__quantity-input');
        const form = wrapper.closest('form');

        const plusBtn = wrapper.querySelector('.product-card__quantity-btn--plus');
        const minusBtn = wrapper.querySelector('.product-card__quantity-btn--minus');

        function updateButtons() {
            const value = parseInt(input.value) || 1;

            if (value <= 1) {
                minusBtn.classList.add('minus-btn-disabled');
            } else {
                minusBtn.classList.remove('minus-btn-disabled');
            }
        }

        plusBtn.addEventListener('click', () => {
            input.value = (parseInt(input.value) || 1) + 1;
            updateButtons();
            form.submit();
        });

        minusBtn.addEventListener('click', () => {
            input.value = Math.max(1, (parseInt(input.value) || 1) - 1);
            updateButtons();
            form.submit();
        });

        input.addEventListener('input', updateButtons);

        updateButtons();
    });
});