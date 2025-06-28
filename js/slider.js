const slides = document.querySelectorAll('.slide');
const sliderBars = document.querySelectorAll('.slider-bar');

let currentIndex = 0;
let interval = 5000;
let lastTime = performance.now();

function updateSlider(index) {
  slides.forEach((slide, i) => {
    slide.classList.toggle('active', i === index);
  });
  sliderBars.forEach((bar, i) => {
    bar.classList.toggle('active', i === index);
  });
  currentIndex = index;
}

function nextSlide() {
  const next = (currentIndex + 1) % slides.length;
  updateSlider(next);
}

function animate(time) {
  if (time - lastTime >= interval) {
    nextSlide();
    lastTime = time;
  }
  requestAnimationFrame(animate);
}

document.addEventListener('DOMContentLoaded', () => {
  updateSlider(currentIndex);

  document.querySelector('.slider-controls').addEventListener('click', (e) => {
    if (e.target.classList.contains('slider-bar')) {
      const index = Array.from(sliderBars).indexOf(e.target);
      updateSlider(index);
      lastTime = performance.now();
    }
  });

  requestAnimationFrame(animate);
});