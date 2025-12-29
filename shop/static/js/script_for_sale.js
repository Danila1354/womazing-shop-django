document.addEventListener("DOMContentLoaded", function () {
    const priceBlocks = document.querySelectorAll('.shop-item__price');

    priceBlocks.forEach(priceBlock => {
        const standard = priceBlock.querySelector('.standard_price');
        const sale = priceBlock.querySelector('.sale_price');

        if (standard && sale) {
            const standardValue = parseFloat(standard.textContent.replace('$', ''));
            const saleValue = parseFloat(sale.textContent.replace('$', ''));

            if (standardValue !== saleValue) {
                priceBlock.classList.add('sale-active');
            }
        }
    });
});

