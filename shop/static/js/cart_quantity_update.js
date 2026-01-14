document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.product-card__quantity-wrapper').forEach(wrapper => {
        const input = wrapper.querySelector('.product-card__quantity-input');
        const form = wrapper.closest('form');

        const plusBtn = wrapper.querySelector('.product-card__quantity-btn--plus');
        const minusBtn = wrapper.querySelector('.product-card__quantity-btn--minus');

        plusBtn.addEventListener('click', () => {
            let value = parseInt(input.value);
            if (isNaN(value) || value < 1) value = 1;
            input.value = value + 1;
            form.submit();
        });

        minusBtn.addEventListener('click', () => {
            let value = parseInt(input.value);
            if (isNaN(value) || value <= 1) value = 2;
            input.value = value - 1;
            form.submit();
        });
    });
});