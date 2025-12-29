const openBtn = document.getElementById("openPopupBtn");
const popup = document.getElementById("popupOverlay");
const closeBtn = document.getElementById("popupClose");

const successPopup = document.getElementById("successPopup");
const successCloseBtn = document.getElementById("successClose");

const form = document.querySelector(".popup-form");

// Открытие основного popup
openBtn.addEventListener("click", () => {
  popup.style.display = "flex";
  document.body.style.overflow = "hidden";
});

// Закрытие основного popup
closeBtn.addEventListener("click", () => {
  popup.style.display = "none";
  document.body.style.overflow = "";
});

// Закрытие success popup
successCloseBtn.addEventListener("click", () => {
  successPopup.style.display = "none";
  document.body.style.overflow = "";
});

// Закрытие по клику вне окна (основной popup)
popup.addEventListener("click", (e) => {
  if (e.target === popup) {
    popup.style.display = "none";
    document.body.style.overflow = "";
  }
});

// Закрытие по клику вне окна (success popup)
successPopup.addEventListener("click", (e) => {
  if (e.target === successPopup) {
    successPopup.style.display = "none";
    document.body.style.overflow = "";
  }
});

// Обработка отправки формы
form.addEventListener("submit", (e) => {
  e.preventDefault();

  // Тут можно добавить валидацию если нужно

  // Скрываем основной popup
  popup.style.display = "none";

  // Показываем success popup
  successPopup.style.display = "flex";

  // Блокируем прокрутку
  document.body.style.overflow = "hidden";

  // Очистка формы (по желанию)
  form.reset();
});
