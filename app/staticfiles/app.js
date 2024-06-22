const closeNotifBtns = document.querySelectorAll(".close-notification");

closeNotifBtns.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    const id = e.target.id.replace("close-btn-", "");
    const notif = document.getElementById(`notif-${id}`);
    notif.remove();
  });
});
