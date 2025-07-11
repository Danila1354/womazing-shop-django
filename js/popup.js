
  const openBtn = document.getElementById("openPopupBtn");
  const popup = document.getElementById("popupOverlay");
  const closeBtn = document.getElementById("popupClose");

  openBtn.addEventListener("click", () => {
    popup.style.display = "flex";
    document.body.style.overflow = "hidden";
  });

  closeBtn.addEventListener("click", () => {
    popup.style.display = "none";
    document.body.style.overflow = "";
  });

  // Закрытие по клику вне окна
  popup.addEventListener("click", (e) => {
    if (e.target === popup) {
      popup.style.display = "none";
      document.body.style.overflow = "";
    }
  });