const swiper = new Swiper('.dream-team__swiper', {
    loop: true,
    navigation: {
        nextEl: '.dream-team__next',
        prevEl: '.dream-team__prev',
    },
    pagination: {
        el: '.dream-team__pagination',
        clickable: true,
        type: 'bullets',
    },
    autoplay: {
    delay: 5000, 
    disableOnInteraction: false, 
    },
    });