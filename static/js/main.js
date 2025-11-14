document.addEventListener('DOMContentLoaded', function () {
  if (typeof Swiper !== 'undefined') {
    const swiper = new Swiper('.heroSwiper', {
      loop: true,
      autoplay: { delay: 5000, disableOnInteraction: false },
      speed: 800,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      slidesPerView: 1,
    });
  } else {
    console.warn('Swiper not loaded');
  }
});

